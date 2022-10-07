import os,argparse,os.path
import re,sys
from template_code import *

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


def generate(dest_variable,template,template_var_dict, extracted_values):
    
    new_path_schema=os.path.join(path,dest_variable)
    if os.path.exists(new_path_schema):
        pass 
    else:
        os.mkdir(new_path_schema)

        print(dest_variable)
        if dest_variable!='graphql_types':
            dest_file=open(f'{package_name}/{dest_variable}/{new_filename}.py','w')

            # for template_var, extracted_var in template_var_dict.items():
            #     template_var='{'+template_var+'}'
            #     template=template.replace(f"${template_var}", extracted_values[extracted_var])
            # dest_file.write(template)

        else:
            
            li_st=['queries','node','mutation']
            if dest_variable=='graphql_types':
                for item in li_st:
                    new_path_node=os.path.join(path,dest_variable,'master_data',item)
                    os.makedirs(new_path_node)

            #         if item!='mutation':
            #             write_file_graphql=open(f'{package_name}/{dest_variable}/master_data/{item}/{new_filename}.py','w')
            #             write_file_init_files=open(f'{package_name}/{dest_variable}/master_data/{item}/__init__.py','w')
                
            #             if item == 'node':
            #                 for template_var, extracted_var in template_var_dict.items():
            #                     template_var='{'+template_var+'}'

            #                     string_txt[0]=string_txt[0].replace(f"${template_var}", extracted_values[extracted_var])
            #                     string_txt[2]=string_txt[2].replace(f"${template_var}", extracted_values[extracted_var])

            #                 write_file_graphql.write(string_txt[0])
            #                 write_file_init_files.write(string_txt[2])

            #             else:
            #                 for template_var, extracted_var in template_var_dict.items():
            #                     template_var='{'+template_var+'}'

            #                     string_txt[1]=string_txt[1].replace(f"${template_var}", extracted_values[extracted_var])
            #                     string_txt[3]=string_txt[3].replace(f"${template_var}", extracted_values[extracted_var])

            #                 write_file_graphql.write(string_txt[1])
            #                 write_file_init_files.write(string_txt[3])

            #         else:
            #             write_file_init_files=open(f'{package_name}/{dest_variable}/master_data/{item}/__init__.py','w')
            #             for template_var, extracted_var in template_var_dict.items():
            #                 template_var='{'+template_var+'}'

            #                 string_txt[4]=string_txt[4].replace(f"${template_var}", extracted_values[extracted_var])
            #             write_file_init_files.write(string_txt[4])
     
for arr in args_split_input:
    extracted_values={
'$package_Name':f"{package_name}", '$class_Name': f"{class_name}" ,'$file_Name':f'{new_filename}'
}
    if arr==args_split_input[0]:
        string_txt=Createschema()
        template_var_dicts = {"classname": "$class_Name"}

    elif arr==args_split_input[1]:
        string_txt=Createcrud()
        template_var_dicts={"package":"$package_Name","classname":"$class_Name","filename":"$file_Name"}

    elif arr==args_split_input[2]:
        string_txt=Createservices()
        template_var_dicts={"package":"$package_Name","classname":"$class_Name","filename":"$file_Name"}

    else:
        string_txt=[CreateGraph_node(),CreateGraph_queries(),CreateGraph_node_init_(),CreateGraph_queries_init_(),CreateGraph_mutation_init_()]
        template_var_dicts={"package":"$package_Name","classname":"$class_Name","filename":"$file_Name"}
        
    generate(arr,string_txt,template_var_dicts,extracted_values)