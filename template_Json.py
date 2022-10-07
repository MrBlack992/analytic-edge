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
my_parser.add_argument('-g','--generate',action="store",type=str,help="This store the name of the folder",required=False)
args=my_parser.parse_args()

args_store_input= sys.argv[3]
args_split_input=args_store_input.split(",")


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

store_generate_value=args.generate
choice=('mas','ud',' ')
args_store_input= sys.argv[3]
args_split_input=args_store_input.split(",")
dest_variable=args_split_input


model_details={"ObjectA":{
"template_code":Createschema(),
"template_var_dict_schema":{"classname": "$class_Name"}
},
"ObjectB":
{
"template_code":Createcrud(),
"template_var_dict_crud":{"package":"$package_Name","classname":"$class_Name","filename":"$file_Name"}
    
},
"ObjectC":{
"template_code":Createservices(),
"template_var_dict_services":{"package":"$package_Name","classname":"$class_Name","filename":"$file_Name"}
},
"destination_path":"f'{package_name}/{dest_variable}/{new_filename}.py'"
}

json_str=json.dumps(model_details,indent=True)
print(type(json_str))
Json_str=json.loads(json_str)
print(type(Json_str))


def generate(dest_variable,template,template_var_dict, extracted_values):
    
    new_path_schema=os.path.join(path,dest_variable)
    if os.path.exists(new_path_schema):
        pass 
    else:
        os.mkdir(new_path_schema)
        
        extracting_path=Json_str['destination_path']

        remove_unwanted_part=extracting_path.replace("\"","")

        convert_to_tuple=eval(remove_unwanted_part)
        again_convert_to_string=''.join(convert_to_tuple)

        dest_file=open(again_convert_to_string,"w")    
        new_string_file=template
        
        for template_var, extracted_var in template_var_dict.items():
            template_var='{'+template_var+'}'
            new_string_file=new_string_file.replace(f"${template_var}", extracted_values[extracted_var])
        dest_file.write(new_string_file)
    
     
for arr in dest_variable:
    extracted_values={'$package_Name':f'{package_name}', '$class_Name': f'{class_name}','$file_Name':f'{new_filename}'}
    if arr==dest_variable[0]:
        string_txt=Json_str['ObjectA']['template_code']
        template_var_dicts = Json_str['ObjectA']['template_var_dict_schema']
        
    elif arr==args_split_input[1]:
        string_txt=Json_str['ObjectB']['template_code']
        template_var_dicts=Json_str['ObjectB']['template_var_dict_crud']
    else:
        string_txt=Json_str['ObjectC']['template_code']
        template_var_dicts=Json_str['ObjectC']['template_var_dict_services']
    
    generate(arr,string_txt,template_var_dicts,extracted_values)