
from graphene_sqlalchemy import (
    SQLAlchemyObjectType
)
from graphene import (
    Int,
    String,
)
from models import (
    funko,
    user,
)


class Funko(SQLAlchemyObjectType):
    class Meta:
        model = funko.Funko
    name = String(description='the name of the funko pop')
    number = Int(description='the number of the funko pop')


class User(SQLAlchemyObjectType):
    class Meta:
        model = user.User
        exclude_fields = ('funko_id', )

