import argparse,os,re


parser=argparse.ArgumentParser()
parser.add_argument('filename',type=argparse.FileType('r'))
args=parser.parse_args()


def getfile():

    file_name=args.filename.name
    # print(type(file_name))
    filename_remove_ext=os.path.splitext(file_name)[0]
    new_filename=filename_remove_ext.split('/')[-1]
    return new_filename

def getpackagename():
    file_path=args.filename.name
    
    package_name=file_path.split('/')[-1]
    return package_name


def getclassname():
    fileopen=open(args.filename.name,'r')
    read_content=fileopen.read()
    
    lis=[]
    pattern=re.compile(r"class\s*([a-zA-Z]+)\(?")
    for match in pattern.finditer(read_content):
        matching=match.group(1)
        lis.append(matching)
    return lis
    
            

if __name__=="__main__":
    """Storing the return value of the functions in variables"""
    store_getfile_value=getfile()
    store_getpackage_vlaue=getpackagename()      
    store_getclass_vlaue=getclassname()

    print(f"The filename is {store_getfile_value} ,and the package name is  {store_getpackage_vlaue} , and the classname is the file is  {store_getclass_vlaue} ")