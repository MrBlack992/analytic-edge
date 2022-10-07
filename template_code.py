
def Createschema():

    var="""from pydantic import BaseModel
class ${classname}CreateSchema(BaseModel):
    pass
class ${classname}UpdateSchema(BaseModel):
    pass
class ${classname}Schema(BaseModel):
    class Config:
        orm_mode = True"""
    
    return var





def Createcrud():
    
    var="""from dde_core.orm import CRUDBase
import  ${package}.models.${filename} as models
import  ${package}.schemas.${filename} as schemas

class CURD${classname}(
    CRUDBase[
        models.${classname},
        schemas.${classname}CreateSchema,
        schemas.${classname}UpdateSchema,
    ]
):
    pass

crud_master_data = CURD${classname}(models.${classname})"""
    return var


def Createservices():

    var="""from logging import getLogger
from typing import Any, Dict, List, Optional
from sqlalchemy.orm import Session

from ${package}.schemas.${filename} import (
    ${classname}CreateSchema,
    ${classname}Schema,
    ${classname}UpdateSchema,
)
from crud.${filename} import crud_master_data


logger = getLogger(__name__)


class ${classname}Service:
    def __init__(self, session: Session) -> None:
        self.session = session


    def get(self, id: int) -> Optional[${classname}]:
        logger.info(f"Fetching master data with id: {id}")
        return crud_master_data.get(
            self.session, id
        )

    def create(self, data: ${classname}CreateSchema) -> ${classname}:
        return crud_master_data.create(self.session, data)

    def update(self, id: int, data: ${classname}UpdateSchema) -> ${classname}:
        master_data = self.get(id)
        return crud_master_data.create(self.session, master_data, data)

    def delete(self, id: int) -> ${classname}:
        return crud_master_data.remove(self.session, id)"""

    return var

def CreateGraph_node():
    var="""from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from ${package}.models.${filename} import ${classname} as MasterDataModel
class ${classname}(SQLAlchemyObjectType):
    class Meta:
        model = MasterDataModel
        interfaces = (relay.Node,)"""
    return var


def CreateGraph_node_init_():
    var="""from .master_data import ${classname}
__all__ = ["${classname}"]
    """
    return var

def CreateGraph_queries():  
    var="""import graphene
from dde_core.db import db
from graphene import ObjectType, relay
from graphene.types.scalars import ID
from ${package}.services.${classname} import MasterData
from ..node.master_data import MasterData

class ${classname}Query(ObjectType):
     master_data = graphene.Field(
    lambda: ${classname},
    args={"id": graphene.Argument(ID, required=True)}
    )
def resolve_master_data(self, info):
    mds = ${classname}Service(db.session)
    return mds.get(id)
    """
    return var


def CreateGraph_queries_init_():
    var="""from .master_data import ${classname}Query
__all__ = ["${classname}Query"]
    """
    return var

def CreateGraph_mutation_init_():
    var="""from graphene.types.objecttype import ObjectType
class MasterDataMutation(ObjectType):
    pass
"""
    return var