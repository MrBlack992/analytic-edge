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

fileopen=open(args.filename.name,'r')
read_content=fileopen.read()
    
pattern=re.compile(r"class\s*([a-zA-Z]+)\(?")
for match_class in pattern.finditer(read_content):
    matching_classname=match_class.group(1)

file_path=args.filename.name
package_name=file_path.split('/')[-3]
path=fr"C:\Users\SiddharthGhatuary\Desktop\task_file\{package_name}"
filename_remove_ext=os.path.splitext(file_path)[0]
new_filename=filename_remove_ext.split('/')[-1]

dictofstrings={
'package':package_name, 'classname':matching_classname,'filename':new_filename
}

def CreateSchema():
        new_path_schema=os.path.join(path,schema_variable)
        if os.path.exists(new_path_schema):
            pass 
        else:
            os.mkdir(new_path_schema)
        
            write_file=open(f'{package_name}/{schema_variable}/{new_filename}.py','w')
            with open('template_schema.py') as new_File:
                lines=new_File.readlines()
                list_to_string=" "
                str_schemas=list_to_string.join(lines)
                new_file=re.sub(pattern="classname",repl=matching_classname,string=str_schemas)
                write_file.write(new_file)

if schema_variable==" ":
    pass
else:
    CreateSchema()


def CreateCrud():
        new_path=os.path.join(path,crud_variable)
        if os.path.exists(new_path):
            pass
        else:
            os.mkdir(new_path)
       
            write_file_crud=open(f'{package_name}/{crud_variable}/crud_{new_filename}.py','w')
            with open('template_crud.txt') as new_file_crud:
                lines=new_file_crud.readlines()
                list_to_string=" "
                string_crud=list_to_string.join(lines)
                for word, initial in dictofstrings.items():
                    string_crud=string_crud.replace(word.lower(),initial)
                write_file_crud.write(string_crud)



store_generate_value=args.generate
choice=('ma',' ')

if store_generate_value.endswith(choice):
    pass
else:
    crud_variable=args_split_input[1]
    if crud_variable==" ":
        pass
    else:
        CreateCrud()




def CreateServices():

        new_path=os.path.join(path,service_variable)
        if os.path.exists(new_path):
            pass
        else:
            os.mkdir(new_path)
            
            write_file_service= open(f'{package_name}/services/service_{new_filename}.py','w')
            with open('template_services.txt') as new_file_services:
                lines=new_file_services.readlines()
                list_to_string=" "
                str_service=list_to_string.join(lines)
            for word, initial in dictofstrings.items():
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
