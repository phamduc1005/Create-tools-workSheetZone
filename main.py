import glob

dict = dict()
typeAuthorization = ['psd', 'svg', 'json', 'jpg']
listImages = []

templates = glob.glob("/home/duc/createToolsWorksheetZone/Create-tools-workSheetZone/hello/*")

for template in templates:
    for type in typeAuthorization:
        pathImage = '{pathImage}/*.{typeImage}'.format(pathImage = template, typeImage = type)
        images = glob.glob(pathImage)
        listImages += images

    keyTemplate = template.split('/')[-1]
    dict.update({ keyTemplate: listImages })
    listImages = []
    
print(dict)
