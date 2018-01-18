import os

dir_name = 'c:/Users/Paul/Desktop/130_0603 - Copy/'
dir_list = os.listdir(dir_name)

for files in dir_list:
    if files.endswith('JPG') and files[:-3] + 'DNG' in dir_list:
        os.remove(dir_name + files)
        print(files, 'deleted')
