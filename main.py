import glob
import re

dict = dict()
list = list()
currentFolder = ''

pathImages = glob.glob("/home/duc/createToolsWorksheetZone/Create-tools-workSheetZone/hello/*/*.jpg")
for index, path in enumerate(pathImages):
    pathImage = path.split('/')
    if index == 0:
        currentFolder = pathImage[-2]

    if currentFolder != pathImage[-2]:
        dict[currentFolder] = list
        currentFolder = pathImage[-2]
        list.clear()
    # findFolderParent = re.search(currentFolder, pathImage[-2])
    else:
        list.append(path)
    if index == len(pathImages) - 1:
        dict[currentFolder] = list
print(dict)
