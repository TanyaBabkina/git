
import os
import shutil

def checkDir(root, dir):
    if root in os.path.abspath(dir):
        return 1
    else:
        print(f'\033[31mНет доступа в данную директроию! \033[39m')
        return 0

class FileManager:
    def __init__(self, root):
        self.root = root
        os.chdir(self.root)

    def create_file(self, fileName):
        filepath = os.path.join(os.getcwd(), fileName)
        if checkDir(self.root, filepath):
            file = open(filepath, "a")
            file.close()
            print(f"\033[32mФайл создан\033[39m")

    
    def create_dir(self, dir_path):
        dirpath = os.path.join(os.getcwd(), dir_path)
        if checkDir(self.root, dirpath):
            os.makedirs(dirpath) 
            print(f"\033[32mДиректория создана\033[39m")

    def delete_dir(self, dir_path):
        # dirpath = os.path.join(os.getcwd(), dir_path)
        dirpath=dir_path
        if checkDir(self.root, dirpath):
            os.removedirs(dirpath)
            print(f"\033[32mДиректория удалена\033[39m")

    def change_dir(self, dir_path):
        if checkDir(self.root,  os.path.join(os.getcwd(), dir_path)):
            os.chdir(dir_path)
            print("Текущая директория: ", os.getcwd())

    def file_input(self, fileName, text):
        filepath = os.path.join(os.getcwd(), fileName)
        if checkDir(self.root, filepath):
            file = open(filepath, "a")
            file.write(text)
            file.close()
            print(f"\033[32mТекст добавлен в файл\033[39m")
    def file_output(self, fileName):
        filepath = os.path.join(os.getcwd(), fileName)
        if checkDir(self.root, filepath):
            file = open(filepath, "r")
            file_data = file.readlines()
            print(''.join(file_data))
            file.close()

    def file_remove(self, fileName):
        filepath = os.path.join(os.getcwd(), fileName)
        if checkDir(self.root, filepath):
            os.remove(filepath)
            print(f"\033[32mФайл удалён\033[39m")

    def file_copy(self, src, dst):
        src_path = os.path.join(os.getcwd(), src)
        dst_path = os.path.join(os.getcwd(), dst)
        if checkDir(self.root, src_path) and checkDir(self.root, dst_path):
            shutil.copy(src_path, dst_path) 
            print(f"\033[32mСделана копия файла\033[39m")
    def file_replace(self, src, dst):
        src_path = os.path.join(os.getcwd(), src)
        dst_path = os.path.join(os.getcwd(), dst)
        if checkDir(self.root, src_path) and checkDir(self.root, dst_path):
            os.replace(src_path, dst_path)
            print(f"\033[32mФайл перемещён\033[39m")
    def file_rename(self, fileName, fileNameNew):
        filepath = os.path.join(os.getcwd(), fileName)
        filepath2 = os.path.join(os.getcwd(), fileNameNew)
        if checkDir(self.root, filepath) and checkDir(self.root, filepath2):
            os.rename(filepath, filepath2)