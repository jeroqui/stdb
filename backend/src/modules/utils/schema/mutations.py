import graphene
from graphene.types.mutation import MutationOptions


'''
I copied django_graphene without the knowledge to do so.
So this might be a disaster. I don't know.

I dindn't want the form to overwrite the arguments class.
'''


class ErrorType(graphene.ObjectType):
    message = graphene.String()
    code = graphene.String()


class FieldErrorsType(graphene.ObjectType):
    field_name = graphene.String()
    field_errors = graphene.List(ErrorType)

class DjangoFormMutationOptions(MutationOptions):
    form_class = None
    model = None

class FormErrorMutation(graphene.Mutation):
    class Meta:
        abstract = True
    
    errors = graphene.List(FieldErrorsType)

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        form_class=None,
        model=None,
        **options,
    ):

        if not form_class:
            raise Exception("form_class is required for DjangoModelFormMutation")

        if not model:
            model = form_class._meta.model

        if not model:
            raise Exception("model is required for DjangoModelFormMutation")
        
        model_name = model.__name__
        return_field_name = model_name[:1].lower() + model_name[1:]

        _meta = DjangoFormMutationOptions(cls)
        _meta.form_class = form_class
        _meta.model = model
        _meta.return_field_name = return_field_name

        super().__init_subclass_with_meta__(
            _meta=_meta, **options
        )


    @classmethod
    def get_form(cls, root, info, **input):
        form_kwargs = cls.get_form_kwargs(root, info, **input)
        return cls._meta.form_class(**form_kwargs)

    @classmethod
    def get_form_kwargs(cls, root, info, **input):
        kwargs = {"data": input['input']}

        pk = input.pop("id", None)
        if pk:
            instance = cls._meta.model._default_manager.get(pk=pk)
            kwargs["instance"] = instance

        return kwargs
    
    @classmethod
    def perform_mutate(cls, form, info):
        obj = form.save()
        kwargs = {cls._meta.return_field_name: obj}
        return cls(errors=[], **kwargs)
    
    @classmethod
    def mutate(cls, root, info, **input):
        form = cls.get_form(root, info, **input)

        if form.is_valid():
            return cls.perform_mutate(form, info)
        else:
            errors_list = []

            for field, errors in form.errors.as_data().items():
                errors_list.append({
                    "field_name": field,
                    "field_errors": [
                        {
                            "message": single_error.message,
                            "code": single_error.code
                        } for single_error in errors
                    ]
                })

            return cls(errors=errors_list)