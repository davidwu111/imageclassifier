import os
import sys

import pyexiv2


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
    yourPath = input('Copy your working folder:')
    if confirmPath(yourPath):
        workingPath = yourPath
    else:
        print('Wrong folder, exiting...')
        sys.exit()
    return workingPath


if __name__ == '__main__':
    print(rootFolder())
