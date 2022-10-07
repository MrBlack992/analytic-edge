import os,argparse,os.path
import re,sys
from template_code import *
from functools import partial

my_parser=argparse.ArgumentParser(description="This show the contents of the file")
my_parser.add_argument('filename',type=argparse.FileType('r'))
my_parser.add_argument('-g','--generate',action="store",type=str,help="This store the name of the folder",required=False)
args=my_parser.parse_args()

args_store_input= sys.argv[3]
args_split_input=args_store_input.split(",")
schema_variable=args_split_input[0]
print(schema_variable)

fileopen=open(args.filename.name,'r')
read_content=fileopen.read()
    
pattern=re.compile(r"class\s*([a-zA-Z]+)\(?")
for match_class in pattern.finditer(read_content):
    class_name=match_class.group(1)

file_path=args.filename.name
package_name=file_path.split('/')[-3]
print(package_name)

path=fr"C:\Users\SiddharthGhatuary\Desktop\task_file\{package_name}"

filename_remove_ext=os.path.splitext(file_path)[0]
new_filename=filename_remove_ext.split('/')[-1]


store_generate_value=args.generate
choice=('mas','ud',' ')
args_store_input= sys.argv[3]
args_split_input=args_store_input.split(",")



def generate(dest_variable,template_var_dicts, extracted_values,string_txt_query,string_txt_query_init_,string_txt_node,string_txt_node_init_,string_txt_mutation_init_):
    

    new_path_schema=os.path.join(path,dest_variable)
    if os.path.exists(new_path_schema):
        pass 
    else:
        os.mkdir(new_path_schema)

        li_st=['queries','node','mutation']
        if arr=='graphql_types':
            for item in li_st:
                new_path_node=os.path.join(path,dest_variable,'master_data',item)

                if os.path.exists(new_path_node):
                    pass
                else:
                    os.makedirs(new_path_node)
                    write_file_graphql=open(f'{package_name}/{schema_variable}/master_data/{item}/{new_filename}.py','w')
                    write_file_init_files=open(f'{package_name}/{schema_variable}/master_data/{item}/__init__.py','w')

# dest_file=open(f'{package_name}/{dest_variable}/{new_filename}.py','w')
                if item=='queries':
                    for template_var, extracted_var in template_var_dicts.items():
                        template_var='{'+template_var+'}'

                        string_txt_query=string_txt_query.replace(f"${template_var}", extracted_values[extracted_var])

                        string_txt_query_init_=string_txt_query_init_.replace(f"${template_var}", extracted_values[extracted_var])


                    write_file_graphql.write(string_txt_query)
                    write_file_init_files.write(string_txt_query_init_)

                elif item == 'node':
                    for template_var, extracted_var in template_var_dicts.items():
                        template_var='{'+template_var+'}'

                        string_txt_node=string_txt_node.replace(f"${template_var}", extracted_values[extracted_var])

                        string_txt_node_init_=string_txt_node_init_.replace(f"${template_var}", extracted_values[extracted_var])

                    write_file_graphql.write(string_txt_node)
                    write_file_init_files.write(string_txt_node_init_)

                else:
                    for template_var, extracted_var in template_var_dicts.items():
                        template_var='{'+template_var+'}'

                        string_txt_mutation_init_=string_txt_mutation_init_.replace(f"${template_var}", extracted_values[extracted_var])
                    write_file_init_files.write(string_txt_mutation_init_)

           

for arr in args_split_input:
    extracted_values={
'$package_Name':package_name, '$class_Name': f"{class_name}" ,'$file_Name':f'{new_filename}'
}       
    if arr==args_split_input[0]:

        string_txt_query=Creategraphqueries()
        string_txt_query_init_=Creategraphqueries_init_()
        string_txt_node=CreateGraph_node()
        string_txt_node_init_=Creategraphnode_init_()
        string_txt_mutation_init_=Createmutation_init_()

        template_var_dicts={"package":"$package_Name","classname":"$class_Name","filename":"$file_Name"}
    else:
        pass

    generate(arr,template_var_dicts,extracted_values,string_txt_query,string_txt_query_init_,string_txt_node,string_txt_node_init_,string_txt_mutation_init_)


# def CreateGraphQl():
#         li_st=['queries','node']
#         for item in li_st:
#             new_path_node=os.path.join(path,schema_variable,'master_data',item)
#             if os.path.exists(new_path_node):
#                 pass 
#             else:
#                 os.makedirs(new_path_node)

#                 write_file=open(f'{package_name}/{schema_variable}/master_data/{item}/{new_filename}.py','w')
#                 write_file_=open(f'{package_name}/{schema_variable}/master_data/{item}/__init__.py','w')
#                 extracted_values={'$package_Name':package_name, '$class_Name': f"{class_name}" ,'$file_Name':f'{new_filename}'}
#                 template_var_dicts={"package":"$package_Name","classname":"$class_Name","filename":"$file_Name"}

#                 if item=='queries':
#                     new_string_file=Creategraphqueries()
#                     new_string_file_=Creategraphqueries_init_()
#                     for template_var, extracted_var in template_var_dicts.items():

#                         template_var='{'+template_var+'}'
#                         new_string_file=new_string_file.replace(f"${template_var}", extracted_values[extracted_var])

#                         new_string_file_=new_string_file_.replace(f"${template_var}", extracted_values[extracted_var])

#                     write_file.write(new_string_file)
#                     write_file_.write(new_string_file_)

#                 elif item=='node':
#                     new_string_file=CreateGraph_node()
#                     new_string_file_=Creategraphnode_init_()
#                     for template_var, extracted_var in template_var_dicts.items():
#                         template_var='{'+template_var+'}'
#                         new_string_file=new_string_file.replace(f"${template_var}", extracted_values[extracted_var])
# #                         new_string_file_=new_string_file_.replace(f"${template_var}", extracted_values[extracted_var])
# #                     write_file.write(new_string_file)
# #                     write_file_.write(new_string_file_)
# #                 else:
# #                     pass
# # CreateGraphQl()


# def CreateGraphQl():
#         li_st=['queries','node']
#         for item in li_st:
#             new_path_node=os.path.join(path,schema_variable,'master_data',item)
#             if os.path.exists(new_path_node):
#                 pass 
#             else:
#                 os.makedirs(new_path_node)
#                 for items in li_st:
#                     outfile=open(items,'w')
#                     li_st_of_files=['master_data','__init__']
#                     for files in li_st_of_files:
#                         outfile_init_=open(f'{package_name}/{schema_variable}/master_data/{item}/{files}.py','w')



        
                # write_file=open(f'{package_name}/{schema_variable}/master_data/{item}/{new_filename}.py','w')
                # write_file_=open(f'{package_name}/{schema_variable}/master_data/{item}/__init__.py','w')


                # extracted_values={'$package_Name':package_name, '$class_Name': f"{class_name}" ,'$file_Name':f'{new_filename}'}
                # template_var_dicts={"package":"$package_Name","classname":"$class_Name","filename":"$file_Name"}

                # if item=='queries':
                #     new_string_file=Creategraphqueries()
                #     new_string_file_=Creategraphqueries_init_()
                #     for template_var, extracted_var in template_var_dicts.items():

                #         template_var='{'+template_var+'}'
                #         new_string_file=new_string_file.replace(f"${template_var}", extracted_values[extracted_var])

                #         new_string_file_=new_string_file_.replace(f"${template_var}", extracted_values[extracted_var])

                #     write_file.write(new_string_file)
                #     write_file_.write(new_string_file_)

                # elif item=='node':
                #     new_string_file=CreateGraph_node()
                #     new_string_file_=Creategraphnode_init_()
                #     for template_var, extracted_var in template_var_dicts.items():
                #         template_var='{'+template_var+'}'
                #         new_string_file=new_string_file.replace(f"${template_var}", extracted_values[extracted_var])
                #         new_string_file_=new_string_file_.replace(f"${template_var}", extracted_values[extracted_var])
                #     write_file.write(new_string_file)
                #     write_file_.write(new_string_file_)
                # else:
                #     pass
