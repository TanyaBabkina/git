
import os
import shutil


def create_file(fileName):
    filepath = os.path.join(os.getcwd(), fileName)
    file = open(filepath, "a")
    file.close()

# create_file("C:\\Users\\1\\Desktop\\FileManagerFolder", "new.txt")
# print('file created')
    
def create_dir(dir_path):
    # if not os.path.isdir(dir_path):
    dirpath = os.path.join(os.getcwd(), dir_path)
    os.makedirs(dirpath)
    print("Текущая директория: ", os.getcwd())    

def delete_dir(dir_path):
    dirpath = os.path.join(os.getcwd(), dir_path)
    os.removedirs(dirpath)

def change_dir(dir_path):
    os.chdir(dir_path)
    print("Текущая директория: ", os.getcwd())

def file_input(fileName, text):
    filepath = os.path.join(os.getcwd(), fileName)
    file = open(filepath, "a")
    file.write(text)
    file.close()
def file_output(fileName):
    filepath = os.path.join(os.getcwd(), fileName)
    file = open(filepath, "r")
    file_data = file.readlines()
    print(''.join(file_data))
    file.close()

def file_remove(fileName):
    filepath = os.path.join(os.getcwd(), fileName)
    os.remove(filepath)

def file_copy(src, dst):
    src_path = os.path.join(os.getcwd(), src)
    dst_path = os.path.join(os.getcwd(), dst)
    shutil.copy(src_path, dst_path) 

def file_replace(src, dst):
    src_path = os.path.join(os.getcwd(), src)
    dst_path = os.path.join(os.getcwd(), dst)   
    os.replace(src_path, dst_path)

def file_rename(fileName, fileNameNew):
    filepath = os.path.join(os.getcwd(), fileName)
    filepath2 = os.path.join(os.getcwd(), fileNameNew)
    os.rename(filepath, filepath2)