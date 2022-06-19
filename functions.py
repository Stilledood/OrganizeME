import os
import shutil


DICT_FILES={
    'Pictures':['jpg','jpeg','png','JPEG'],
    'Video':['mp4', 'mov', 'MOV','avi'],
    'PDF':['pdf','PDF'],
    'Text':['txt'],
    'Music':['mp3'],
    'Python':['py'],
    'Word Files':['doc','docx'],
    'Executables':['exe'],
    'Archives':['zip','7z'],
    'Databases':['csv']
}

def path_validation(path:str) -> bool:
    '''Function to check if the path is a corect path'''
    return os.path.isdir(path)

def extract_files(path:str)->list:
    '''Function that takes a path a return a list of path for all files inside that path'''

    files_list=[file for  file in os.listdir(path) ]
    return files_list

def extract_file_extension(file:str)->str:
    '''Function that takes a file path and return file extension'''
    return file.split('.')[-1]


def create_dirs(path:str,name:str):
    '''Function to check if a directory exists and if not it creates the directory'''
    if not os.path.isdir(path+'\\'+name):
        os.makedirs(path+'\\'+name)


def run(path:str):
    '''Main Function to process all logic'''

    filelist=extract_files(path)
    print(filelist)
    for file in filelist:
        extension=extract_file_extension(file)
        print(extension)
        for name,val in DICT_FILES.items():
            if extension in val:
                create_dirs(path,name)
                shutil.move(path+'\\'+file,path+'\\'+name)


create_dirs(r"C:\Users\User\Downloads",'name')