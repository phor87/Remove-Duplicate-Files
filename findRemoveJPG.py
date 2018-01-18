import os


def checkforfiles(path):

    for items in os.listdir(path):  # iterate dir in working path
        if os.path.isdir(path + items):  # if the unc is a directory
            checkforfiles(path + items + '/')
        else:
            if items.endswith('JPG') and items[:-3] + 'DNG' in os.listdir(path):  # if filename has both extensions
                print('Deleting', items)  # prints what file to be deleted
                os.remove(path + items)  # removes filename.JPG


#  checkforfiles('c:/Users/Paul/Desktop/year/')

