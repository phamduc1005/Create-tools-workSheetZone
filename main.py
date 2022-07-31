import glob
import re

list = []

pathImages = glob.glob("/home/duchungpham/Create-tools-workSheetZone/read-folder-get-image-name/hello/*/*.jpg")
for path in pathImages:
    x = path.split('/')
    x = re.search('hi', x[-2])

    # print(x[-1])
    if x:
        print(x)

# print(pathImages)
