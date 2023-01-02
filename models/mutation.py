from graphene import (
    ObjectType,
    Mutation,
    Int,
    String,
    Field,
)
from api_config import (
    db,
)

from .objects import (
    Funko as FunkoObject,
    User as UserObject,
)
from .funko import Funko as FunkoModel


class createFunko(Mutation):
    class Arguments:
        number = Int(required=True)
        name = String(required=True)
        collection = String(required=True)
    
    funko = Field(lambda: FunkoObject)

    def mutate(self, info, number, name, collection):
        funko = FunkoModel(number=number, name=name, collection=collection)

        db.session.add(funko)
        db.session.commit()

        return createFunko(funko=funko)

class updateFunko(Mutation):
    class Arguments:
        funko_id = Int(required=True)
        collection = String(required=True)

    funko = Field(lambda: FunkoObject)

    def mutate(self, info, collection, funko_id):
        funko = FunkoModel.query.get(funko_id)
        if funko:
            funko.collection = collection
            db.session.add(funko)
            db.session.commit()

        return updateFunko(funko=funko)


class deleteFunko(Mutation):
    class Arguments:
        funko_id = Int(required=True)

    funko = Field(lambda: FunkoObject)

    def mutate(self, info, funko_id):
        funko = FunkoModel.query.get(funko_id)
        if funko:
            db.session.delete(funko)
            db.session.commit()

        return deleteFunko(funko=funko)

class Mutation(ObjectType):
    create_funko = createFunko.Field()
    update_funko = updateFunko.Field()
    delete_funko = deleteFunko.Field()
