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
            datetime = exifData['Exif.Image.DateTime']
            if len(datetime) > 3:
                result[file] = datetime
            else:
                result[file] = 'NA'
    # Read file modified time if EXIF info not available.
    for file, date in result.items():
        if date == 'NA':
            result[file] = readModifyTime(file)
    return result


def readModifyTime(filepath):
    timeFloat = os.path.getmtime(filepath)
    timeStruct = time.localtime(timeFloat)


    return timeFinal
