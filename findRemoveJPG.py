import os

def findremovejpg(path):

    dir_name = path
    dir_list = os.listdir(dir_name)  # list created from dir of folder path

    for files in dir_list:
        if files.endswith('JPG') and files[:-3] + 'DNG' in dir_list:  # if filename has both JPG and DNG extensions
            print('Deleting', files)  # prints what file to be deleted
            os.remove(dir_name + files)  # removes filename.JPG


#findremovejpg('c:/Users/Paul/Desktop/test1/')