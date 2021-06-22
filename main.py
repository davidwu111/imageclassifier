import os
import pyexiv2

# Confirm the working directory. By default the working directory is the same folder as this script.
defaultPath = os.getcwd()
changePath = input('Do you want to change working folder? (Y/N)')
if changePath == 'Y':
    workingPath = input('Copy your working folder:')
else:
    workingPath = defaultPath

if __name__ == '__main__':
    print(defaultPath)
