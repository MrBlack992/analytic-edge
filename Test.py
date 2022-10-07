from genericpath import exists
import os,argparse,os.path
import re,sys
from template_code import *
import json

def getting_arguments():
    my_parser=argparse.ArgumentParser(description="This show the contents of the file")
    my_parser.add_argument('filename',type=argparse.FileType('r'))
    my_parser.add_argument('-g','--template',action="store",type=str,help="This store the name of the folder",required=False)
    args=my_parser.parse_args()
    return args


def find_classname():
    args=getting_arguments()
    fileopen=open(args.filename.name,'r')
    read_content=fileopen.read()
    pattern=re.compile(r"class\s*([a-zA-Z]+)\(?")
    for match_class in pattern.finditer(read_content):
        name=match_class.group(1)
        return name

def find_package_name():
    args=getting_arguments()
    file_path=args.filename.name
    package_name=file_path.split('/')[-3]
    return package_name


def filename():
    args=getting_arguments()
    file_path=args.filename.name
    filename_remove_ext=os.path.splitext(file_path)[0]
    new_filename=filename_remove_ext.split('/')[-1]
    return new_filename


def extract_dest_variable():
    str=" "
    convert_str=str.join(sys.argv)
    pattern_str=re.compile(r"--template\s*([a-zA-Z_]+)")
    dest_var=re.findall(pattern_str,convert_str)
    return dest_var


def main(dest_variable,load_file):
    path=fr"C:\Users\SiddharthGhatuary\Desktop\task_file\{package_name}"
    new_path_schema=os.path.join(path,dest_variable)

    if os.path.exists(new_path_schema):
        pass 
    else:
        os.mkdir(new_path_schema)

        new_file=load_file.read()
        Json_str=json.loads(new_file)

        
        if dest_variable!='graphql_types':

            store_dic=Json_str['destination_folder']
            convert_to_tuple=eval(store_dic)
            again_convert_to_string=''.join(convert_to_tuple)

            new_str_file=Json_str['code']
            template=" ".join(new_str_file)

            template_var_dicts=Json_str['template_vars']

            dest_file=open(again_convert_to_string,'w')

            for template_var, extracted_var in template_var_dicts.items():
                template_var='{'+template_var+'}'
                template=template.replace(f"${template_var}", extracted_values[extracted_var])
            dest_file.write(template)

        else:
            li_st=['node','queries','mutation']
            if dest_variable=='graphql_types':
                for item in li_st:
                    new_path_node=os.path.join(path,dest_variable,'master_data',item)
                    os.makedirs(new_path_node)

                    store_dic=Json_str['destination_folder']
                    store_dic_init_=Json_str['destination_folder_init_']
                    convert_to_tuple=eval(store_dic)
                    convert_to_tuple_init_=eval(store_dic_init_)
                    again_convert_to_string=''.join(convert_to_tuple)
                    again_convert_to_string_init_=''.join(convert_to_tuple_init_)
                    template_var_dicts=Json_str['template_vars']

                    if item!='mutation':                       
                        write_file_graphql=open(again_convert_to_string,'w')
                        write_file_init_files=open(again_convert_to_string_init_,'w')

                        if item == 'node':
                            new_str_file=Json_str['node']['code']
                            new_str_file_init=Json_str['node']['code_init_']
                            template=" ".join(new_str_file)
                            template_init_=" ".join(new_str_file_init)

                            for template_var, extracted_var in template_var_dicts.items():
                                template_var='{'+template_var+'}'
                                template=template.replace(f"${template_var}", extracted_values[extracted_var])
                                template_init_=template_init_.replace(f"${template_var}", extracted_values[extracted_var])

                            write_file_graphql.write(template)
                            write_file_init_files.write(template_init_)
                        
                        else:
                            new_str_file=Json_str['queries']['code']
                            new_str_file_init=Json_str['queries']['code_init_']
                            template=" ".join(new_str_file)
                            template_init_=" ".join(new_str_file_init)

                            for template_var, extracted_var in template_var_dicts.items():
                                template_var='{'+template_var+'}'
                                template=template.replace(f"${template_var}", extracted_values[extracted_var])
                                template_init_=template_init_.replace(f"${template_var}", extracted_values[extracted_var])

                            write_file_graphql.write(template)
                            write_file_init_files.write(template_init_)


                    else:
                        write_file_init_files=open(again_convert_to_string_init_,'w')
                        new_str_file_init=Json_str['mutation']['code_init_']
                        template_init_=" ".join(new_str_file_init)

                        for template_var, extracted_var in template_var_dicts.items():
                                template_var='{'+template_var+'}'
                                template_init_=template_init_.replace(f"${template_var}", extracted_values[extracted_var])
                        
                        write_file_init_files.write(template_init_)

if __name__=="__main__":

    dest_var=extract_dest_variable()
    package_name=find_package_name()
    new_filename=filename()
    class_name=find_classname()
    

    str=" "
    dest_variable=str.join(dest_var)
    
    for var in dest_var:
        extracted_values={'$package_Name':f'{package_name}', '$class_Name': f'{class_name}','$file_Name':f'{new_filename}'}

        if var == dest_var[0]:
            load_file=open('schema.json')
    
        elif var == dest_var[1]:
            load_file=open('crud.json')
    
        elif var == dest_var[2]:
            load_file=open('services.json')

        else:
            load_file=open('graphql.json')
    
        main(var,load_file)
