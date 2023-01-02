from graphene import (
    ObjectType,
    List,
    String,
    Int,
)
from models import (
    funko,
    # user,
)
from models.objects import (
    Funko as FunkoObject,
    User as UserObject
)


class Query(ObjectType):

    funkos = List(lambda: FunkoObject, collection=String(), name=String(), number=Int())
    users = List(lambda: UserObject)


    def resolve_funkos(self, info, collection=None, name=None, number=None):
        query = FunkoObject.get_query(info=info)
        if collection:
            query = query.filter(funko.Funko.collection == collection)
        if name:
            query = query.filter(funko.Funko.name == name)
        if number:
            query = query.filter(funko.Funko.number == number)
        return query.order_by('number').all()
    
    def resolve_users(self, info):
        query = UserObject.get_query(info=info)
        return query.all()
