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


# Get number of image files.


if __name__ == '__main__':
    testpath = input('your path:').strip()
    path = os.path.abspath(testpath)
    tempList = os.walk(testpath)
    for a, b, c in tempList:
        print(a)
        print(b)
        print(c)
    aaa = 1
