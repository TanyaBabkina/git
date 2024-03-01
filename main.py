from FileManager import *




root = "C:\\Users\\1\\Desktop\\FileManagerFolder"
os.chdir(root)

while True:
    command = input(f"\033[34m{os.getcwd()} = > \033[39m").split()
    
    if (command[0] == 'createDir'):
        create_dir(command[1])
    elif (command[0] == 'deleteDir'):
        delete_dir(command[1])
    elif (command[0] == 'changeDir'):
        change_dir(command[1])
    elif (command[0] == 'createFile'):
        create_file(command[1])
    elif (command[0] == 'fileInput'):
        file_input(command[1], ' '.join(command[2:]))
    elif (command[0] == 'fileOutput'):
        file_output(command[1])
    elif (command[0] == 'fileRemove'):
        file_remove(command[1])
    elif (command[0] == 'fileCopy'):
        file_copy(command[1], command[2])
    elif (command[0] == 'fileReplace' ):
        file_replace(command[1], command[2])
    elif (command[0] == 'fileRename'):
        file_rename(command[1], command[2])
    elif (command[0] == 'stop'):
        break
    
    