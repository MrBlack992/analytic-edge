from ast import parse
from genericpath import exists
from hashlib import new
from msilib import schema
from pydoc import describe
import os,argparse,os.path
import re,sys



my_parser=argparse.ArgumentParser(description="This show the contents of the file")
my_parser.add_argument('filename',type=argparse.FileType('r'))
# group = my_parser.add_argument_group()
my_parser.add_argument('-g','--generate',action="store",type=str,help="This store the name of the folder",required=False)

args=my_parser.parse_args()


args_store_input= sys.argv[3]
args_split_input=args_store_input.split(",")

schema_variable=args_split_input[0]

# service_variable=args_split_input[2]



def CreateSchema():
    fileopen=open(args.filename.name,'r')
    read_content=fileopen.read()
    
    pattern=re.compile(r"class\s*([a-zA-Z]+)\(?")
    for match_class in pattern.finditer(read_content):
        matching_classname=match_class.group(1)


        store_path_name=schema_variable
        file_path=args.filename.name
        package_name=file_path.split('/')[-3]
        path=fr"C:\Users\SiddharthGhatuary\Desktop\task_file\{package_name}"
        new_path=os.path.join(path,store_path_name)
        if os.path.exists(new_path):
            pass 
        else:
            os.mkdir(new_path)
        


            filename_remove_ext=os.path.splitext(file_path)[0]
            new_filename=filename_remove_ext.split('/')[-1]
            write_file=open(f'{package_name}/{store_path_name}/{new_filename}.py','w')
            str_file="""from pydantic import BaseModel
class classnameCreateSchema(BaseModel):
    pass
class classnameUpdateSchema(BaseModel):
    pass
class classnameSchema(BaseModel):
    class Config:
        orm_mode = True
    """
            new_file=re.sub(pattern="classname",repl=matching_classname,string=str_file)
            write_file.write(new_file)

if schema_variable==" ":
    pass
else:
    CreateSchema()




def CreateCrud():

    fileopen=open(args.filename.name,'r')
    read_content=fileopen.read()
    
    pattern=re.compile(r"class\s*([a-zA-Z]+)\(?")
    for match_class in pattern.finditer(read_content):
        matching_classname=match_class.group(1)

        store_pathname=crud_variable
        file_path=args.filename.name
        package_name=file_path.split('/')[-3]
        path=fr"C:\Users\SiddharthGhatuary\Desktop\task_file\{package_name}"
        new_path=os.path.join(path,store_pathname)
        if os.path.exists(new_path):
            pass
        else:
            os.mkdir(new_path)
        
            filename_remove_ext=os.path.splitext(file_path)[0]
            new_filename=filename_remove_ext.split('/')[-1]

            write_file_crud=open(f'{package_name}/{store_pathname}/crud_{new_filename}.py','w')
            string_crud="""from dde_core.orm import CRUDBase
import  package.models.filename as models
import  package.schemas.filename as schemas

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
            for word, initial in {"package":package_name, "classname":matching_classname,"filename":new_filename}.items():
                string_crud=string_crud.replace(word.lower(),initial)
            write_file_crud.write(string_crud)



store_generate_value=args.generate
choice=('ma',' ')
if store_generate_value.endswith(choice):
    pass
else:
    crud_variable=args_split_input[1]
    print(crud_variable)
    if crud_variable==" ":
        pass
    else:
        CreateCrud()




def CreateServices():
    fileopen=open(args.filename.name,'r')
    read_content=fileopen.read()
    
    pattern=re.compile(r"class\s*([a-zA-Z]+)\(?")
    for match_class in pattern.finditer(read_content):
        matching_classname=match_class.group(1)



        store_pathname=service_variable
        file_path=args.filename.name
        package_name=file_path.split('/')[-3]
        path=fr"C:\Users\SiddharthGhatuary\Desktop\task_file\{package_name}"
        new_path=os.path.join(path,store_pathname)
        if os.path.exists(new_path):
            pass
        else:
            os.mkdir(new_path)


            filename_remove_ext=os.path.splitext(file_path)[0]
            new_filename=filename_remove_ext.split('/')[-1]
            write_file_service= open(f'{package_name}/services/service_{new_filename}.py','w')
            str_service="""
from logging import getLogger
from typing import Any, Dict, List, Optional
from sqlalchemy.orm import Session

from package.schemas.filename import (
    classnameCreateSchema,
    classnameSchema,
    classnameUpdateSchema,
)
from crud.crud_filename import crud_master_data


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
            for word, initial in {"package":package_name, "classname":matching_classname,"filename":new_filename}.items():
                str_service=str_service.replace(word.lower(),initial)
            write_file_service.write(str_service)



choices=('ma','ud',' ')
if store_generate_value.endswith(choices):
    pass
else:
    service_variable=args_split_input[2]
    if service_variable==" ":
        pass
    else:
        CreateServices()

