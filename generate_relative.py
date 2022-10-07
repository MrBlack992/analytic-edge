import os
import script_file,re


def createSchemas(class_name):
    file_exists=os.path.exists(r'C:\Users\SiddharthGhatuary\Desktop\task_file\schemas')
    if file_exists:
        pass
    else:
        os.mkdir(r'C:\Users\SiddharthGhatuary\Desktop\task_file\schemas')

    write_file=open(f'schemas/master_data.py','w')
    str_file="""
from pydantic import BaseModel
class classnameCreateSchema(BaseModel):
    pass
class classnameUpdateSchema(BaseModel):
    pass
class classnameSchema(BaseModel):
    class Config:
        orm_mode = True
    """

    lis=re.sub(pattern="classname",repl=class_name,string=str_file)
    write_file.write(lis)
    write_file.close()


for i in script_file.getclassname():
    createSchemas(i)





    
def createCrud(crud_name):
    file_exists=os.path.exists(r'C:\Users\SiddharthGhatuary\Desktop\task_file\crud')
    if file_exists:
        pass
    else:
        os.mkdir(r'C:\Users\SiddharthGhatuary\Desktop\task_file\crud')

    write_file_crud=open(f'crud/crud_entity_name.py','w')
    string_crud="""
from dde_core.orm import CRUDBase
import models.modelname as models
import schemas.classname as schemas
class CURDclassname(
    CRUDBase[
        models.classname,
        schemas.classnameCreateSchema,
        schemas.classnameUpdateSchema,
    ]
):
    pass
crud_master_data = CURDclassname(models.classname)
    """
    lis_crud=re.sub(pattern="classname",repl=crud_name,string=string_crud)
    write_file_crud.write(lis_crud)
    write_file_crud.close()

for crud_name in script_file.getclassname():
    createCrud(crud_name)







def createService(service_name):
    file_exists=os.path.exists(r'C:\Users\SiddharthGhatuary\Desktop\task_file\services')
    if file_exists:
        pass
    else:
        os.mkdir(r'C:\Users\SiddharthGhatuary\Desktop\task_file\services')
    write_file_service= open(f'services/master_data_service.py','w')
    str_service="""
from logging import getLogger
from typing import Any, Dict, List, Optional
from sqlalchemy.orm import Session

from schemas.master_data import (
    classnameCreateSchema,
    classnameSchema,
    classnameUpdateSchema,
)
from crud.master_data import crud_master_data
logger = getLogger(__name__)
class classnameService:
    def __init__(self, session: Session) -> None:
        self.session = session
    def get(self, id: int) -> Optional[classname]:
        logger.info(f"Fetching master data with id: {id}")
        return crud_master_data.get(
            self.session, id
        )
    def create(self, data: classnameCreateSchema) -> classname:
        return crud_master_data.create(self.session, data)
    def update(self, id: int, data: classnameUpdateSchema) -> classname:
        master_data = self.get(id)
        return crud_master_data.create(self.session, master_data, data)
    def delete(self, id: int) -> classname:
        return crud_master_data.remove(self.session, id)
    """
    lis_service=re.sub(pattern="classname",repl=service_name,string=str_service)
    write_file_service.write(lis_service)

for i in script_file.getclassname():
    createService(i)
