import sys,os,re

def getfilename():
    file_path=sys.argv[0],sys.argv[1]
    # print(sys.argv[1])
    # print(type(sys.argv[1]))
    # print(file_path)
    (a,b)=file_path
    # print(sys.argv[1].split('\\')[-1])
    return b


def getdirname(c):
    dir=os.path.basename(os.path.dirname(c))
    return dir
# getdirname()
    
def getclassname(d):
    f=open(d,'r')
    content=f.readlines()
    count=0

    for line in content:
        count+=1
            # print("Line{}: {}".format(count,line.strip()))
        match=re.search(r'class\s*([a-zA-Z])\(?',line)
        if match:
            class_names=line
            print(class_names)
        # return class_names
    # getclassname()



if __name__=="__main__":
    file_path=getfilename()
    filename=file_path.split('\\')[-1]
    """Taking the filepath from the getfilname() and storing it in the variable file_path"""

    package_name=getdirname(file_path)
    """Passing the return value of getfilename() to getdirname() that is passing a func as a paramater to another func and then extracting the package name"""

    classname=getclassname(file_path)
    """Finally extracting the classname from the given file"""

    print ("The filename is  {} ,and the package name is  {} , and the classname is the file is  {} ".format(filename,package_name,classname))

    

