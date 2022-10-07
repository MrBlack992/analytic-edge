
from ast import arg, parse
from genericpath import exists
from hashlib import new
from msilib import schema
from pydoc import describe
import os,argparse,os.path
import re,sys
from template_code import *
import json


my_parser=argparse.ArgumentParser(description="This show the contents of the file")
my_parser.add_argument('filename',type=argparse.FileType('r'))
# group = my_parser.add_argument_group()
my_parser.add_argument('-g','--template',action="store",type=str,help="This store the name of the folder",required=False)
args=my_parser.parse_args()


#Open models/master_data.py and read the code and extract the classname,filename and packagename
fileopen=open(args.filename.name,'r')
read_content=fileopen.read()

#finding the classname
    
pattern=re.compile(r"class\s*([a-zA-Z]+)\(?")
for match_class in pattern.finditer(read_content):
    class_name=match_class.group(1)

#finding the package_name
file_path=args.filename.name
package_name=file_path.split('/')[-3]
path=fr"C:\Users\SiddharthGhatuary\Desktop\task_file\{package_name}"

    
#finding the filename
filename_remove_ext=os.path.splitext(file_path)[0]
new_filename=filename_remove_ext.split('/')[-1]

destination_schema=sys.argv[3]
dest_variable_schema=os.path.splitext(destination_schema)[0]



extracted_values={'$package_Name':f'{package_name}', '$class_Name': f'{class_name}','$file_Name':f'{new_filename}'}
def CreateSchema():
    if destination_schema!='':
        new_path_schema=os.path.join(path,dest_variable_schema)
        if os.path.exists(new_path_schema):
            pass 
        else:
            os.mkdir(new_path_schema)
            
            load_schema_json=open('schema.json')
            new_schema_file=load_schema_json.read()

            Json_str=json.loads(new_schema_file)

            store_dic=Json_str['destination_folder']

            convert_to_tuple=eval(store_dic)
            again_convert_to_string=''.join(convert_to_tuple)

            dest_file=open(again_convert_to_string,'w')
            string_txt=Json_str['code']

            new_string_file=" ".join(string_txt)

            template_var_dict=Json_str['template_vars']
            for template_var, extracted_var in template_var_dict.items():
                template_var='{'+template_var+'}'
                new_string_file=new_string_file.replace(f"${template_var}", extracted_values[extracted_var])
            dest_file.write(new_string_file)

           
CreateSchema()

def CreateCrud():
    destination_crud=sys.argv[5]
    dest_variable_crud=os.path.splitext(destination_crud)[0]
    new_path_schema=os.path.join(path,dest_variable_crud)
    if os.path.exists(new_path_schema):
        pass 
    else:
        os.mkdir(new_path_schema)
        load_schema_json=open('crud.json')
        new_schema_file=load_schema_json.read()

        Json_str=json.loads(new_schema_file)

        store_dic=Json_str['destination_folder']

        convert_to_tuple=eval(store_dic)
        again_convert_to_string=''.join(convert_to_tuple)

        dest_file=open(again_convert_to_string,'w')
        
        string_txt=Json_str['code']

        new_string_file=" ".join(string_txt)

        template_var_dict=Json_str['template_vars']
        for template_var, extracted_var in template_var_dict.items():
            template_var='{'+template_var+'}'
            new_string_file=new_string_file.replace(f"${template_var}", extracted_values[extracted_var])
        dest_file.write(new_string_file)

choices=('ma',' ')
if dest_variable_schema.endswith(choices):
    pass
else:

    CreateCrud()

# def CreateServices():
#     destination_services=sys.argv[7]
#     dest_variable_services=os.path.splitext(destination_services)[0]
#     new_path_schema=os.path.join(path,dest_variable_services)
#     if os.path.exists(new_path_schema):
#         pass 
#     else:
#         os.mkdir(new_path_schema)
#         load_schema_json=open('services.json')
#         new_schema_file=load_schema_json.read()

#         Json_str=json.loads(new_schema_file)

#         store_dic=Json_str['destination_folder']

#         convert_to_tuple=eval(store_dic)
#         again_convert_to_string=''.join(convert_to_tuple)

#         dest_file=open(again_convert_to_string,'w')
#         string_txt=Json_str['code']

#         new_string_file=" ".join(string_txt)

#         template_var_dict=Json_str['template_vars']
#         for template_var, extracted_var in template_var_dict.items():
#             template_var='{'+template_var+'}'
#             new_string_file=new_string_file.replace(f"${template_var}", extracted_values[extracted_var])
#         dest_file.write(new_string_file)

# # choices=('ma',' ')
# # if dest_variable_schema.endswith(choices):
# #     pass
# # else:
# #     destination_crud=sys.argv[5]
# #     dest_variable_crud=os.path.splitext(destination_crud)[0]
# #     print(dest_variable_crud)
# #     if dest_variable_crud==" ":
# #         pass
# #     else:

# # CreateServices()

