import pyexiv2
import time
import os


def readEXIF(filelist):
    result = {}
    # Read the EXIF info and input into dict 'result'
    # The date format from EXIF is 2019:05:22 11:05:55
    for file in filelist:
        with pyexiv2.Image(file) as img:
            exifData = img.read_exif()
            try:
                datetime = exifData['Exif.Image.DateTime']
            except:
                result[file] = 'NA'
            else:
                result[file] = datetime
    # Read file modified time if EXIF info not available.
    for file, date in result.items():
        if date == 'NA':
            result[file] = readModifyTime(file)
    return result


def readModifyTime(filepath):
    # The time get from os.path is in float format
    timeFloat = os.path.getmtime(filepath)
    # Convert float time format to a time struct
    timeStruct = time.localtime(timeFloat)
    # Conver time struct to the same format as EXIF extracted.
    timestring = time.strftime('%Y:%m:%d %H:%M:%S', timeStruct)
    return timestring
