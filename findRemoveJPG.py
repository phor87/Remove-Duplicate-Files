import os

def findremovejpg(path):

    dir_name = path
    dir_list = os.listdir(dir_name)

    for files in dir_list:
        if files.endswith('JPG') and files[:-3] + 'DNG' in dir_list:
            os.remove(dir_name + files)
            print(files, 'deleted')

#findremovejpg('c:/Users/Paul/Desktop/test1/')