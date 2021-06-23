import os
import sys


# Confirm the working path is eligible.
def confirmPath(path):
    if len(path) == 0:
        return False
    elif os.path.exists(path):
        return True
    else:
        return False


# Get the working directory.
def rootFolder():
    yourPath = input('Copy your working folder:').strip()
    if confirmPath(yourPath):
        workingPath = os.path.abspath(yourPath)
    else:
        print('Wrong folder, exiting...')
        sys.exit()
    return workingPath


# Get a list of images in tuple.
def photoList(path):
    # Generate a tuple include all files and folders. it yields a 3-tuple (dirpath, dirnames, filenames)
    fullList = os.walk(path, True)
    supportedFormat = ('.jpg', '.jpeg')
    finallist = list()
    # Check each file for the file format.
    for dirpath, dirnames, filenames in fullList:
        for filename in filenames:
            fullPath = os.path.join(dirpath, filename)
            # Seperate file path with file extension
            fileExtension = os.path.splitext(fullPath)
            # Check if the file is image format.
            for ext in fileExtension:
                for supportedExt in supportedFormat:
                    if ext == supportedExt:
                        finallist.append(fullPath)
    return finallist


# Get number of image files.
def getImageCount(list):
    return len(list)


if __name__ == '__main__':
    workingPath = rootFolder()
    photoList = photoList(workingPath)
    print(len(photoList))
    aaa = 1
