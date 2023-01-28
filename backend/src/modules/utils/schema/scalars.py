from graphene import Scalar

from graphql import Undefined
from graphql.language.ast import StringValueNode

from ..hashids import to_db_id

class PublicId(Scalar):
    """
    The public `Id` the client can see.
    """

    @staticmethod
    def parse_literal(ast, _variables=None):
        if isinstance(ast, StringValueNode):
            return to_db_id(ast.value)
        return Undefined
    
    def parse_value(value):
        return to_db_id(value)


