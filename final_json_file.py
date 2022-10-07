import os,argparse,os.path
import re,sys
from template_code import *
import json

my_parser=argparse.ArgumentParser(description="This show the contents of the file")
my_parser.add_argument('filename',type=argparse.FileType('r'))
my_parser.add_argument('-g','--template',action="store",type=str,help="This store the name of the folder",required=False)
args=my_parser.parse_args()

fileopen=open(args.filename.name,'r')
read_content=fileopen.read()

pattern=re.compile(r"class\s*([a-zA-Z]+)\(?")
for match_class in pattern.finditer(read_content):
    class_name=match_class.group(1)

file_path=args.filename.name
package_name=file_path.split('/')[-3]
path=fr"C:\Users\SiddharthGhatuary\Desktop\task_file\{package_name}"

filename_remove_ext=os.path.splitext(file_path)[0]
new_filename=filename_remove_ext.split('/')[-1]
 
def generate(dest_variable,load_file):
     new_path_schema=os.path.join(path,dest_variable)
     if os.path.exists(new_path_schema):
        pass 
     else:
        os.mkdir(new_path_schema)
        
        new_schema_file=load_file.read()
        Json_str=json.loads(new_schema_file)
        
        new_str_file=Json_str['code']
        template=" ".join(new_str_file)
        print(type(template))
        print(template)

        template_var_dicts=Json_str['template_vars']

        store_dic=Json_str['destination_folder']
        convert_to_tuple=eval(store_dic)
        again_convert_to_string=''.join(convert_to_tuple)
        dest_file=open(again_convert_to_string,'w')
        
        for template_var, extracted_var in template_var_dicts.items():
            template_var='{'+template_var+'}'
            template=template.replace(f"${template_var}", extracted_values[extracted_var])
        dest_file.write(template)

extracted_values={'$package_Name':f'{package_name}', '$class_Name': f'{class_name}','$file_Name':f'{new_filename}'}
def CreateSchema():
    destination_schema=sys.argv[3]
    dest_variable=os.path.splitext(destination_schema)[0]
    load_file=open('schema.json')
    generate(dest_variable,load_file)
CreateSchema()

def CreateCrud():
    destination_crud=sys.argv[5]
    dest_variable=os.path.splitext(destination_crud)[0]
    load_file=open('crud.json')
    generate(dest_variable,load_file)
for arr in sys.argv:
    if arr.endswith('ud'):
        CreateCrud()
    else:
        pass

def CreateServices():
    destination_services=sys.argv[7]
    dest_variable=os.path.splitext(destination_services)[0]
    load_file=open('services.json')
    generate(dest_variable,load_file)
for arr in sys.argv:
    if arr.endswith('es'):
        CreateServices()
    else:
        pass

