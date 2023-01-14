from src.modules.utils.hashids import to_db_id, to_public_id

class GlobalidMiddleware(object):
    def resolve(self, next, root, info, **args):
        value = next(root, info, **args)
        if info.field_name == 'id':
            value = to_public_id(info.parent_type.graphene_type._meta.model, value)
        
        return value
