import os
from PIL import Image

def load_image(image_path) :
    # read image from image_path and return image object
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print("Exception from read image: ", image_path, " ", e)
        return None

def isImageFile(file_path):
    # return True if it is image and opposite
    extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
    return file_path.lower().endswith(extensions)

def getImageList(folder_path):
    image_list = []
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        filesName = os.listdir(folder_path)
        for fileName in filesName:
            filePath = os.path.join(folder_path, fileName)
            if isImageFile(filePath) and os.path.isfile(filePath):
                img = load_image(filePath)
                image_list.append(img)
    return image_list