##### Read many image from folder
# Import class image
from PIL import Image
from ImageTool import *
from IPython.display import display
# Folder contain image
mydir = 'D:/Python/computervision/image/01'

# Image path
# image_path = dir + '/1.JPG'
# print(image_path)

# Use funtion 
# img01 = load_image(image_path)

# Read many image
imgs = getImageList(mydir)
#Show all image in folder by funtion display
for img in imgs:
    display(img)

# Show image
# imgs.show()

# Định dạng ảnh
# print("Định dạng ảnh: " , img01.format)
# print size
# print("size: ", img01.size)

# Save image and change
# new_image01_path = dir + '/new_01.JPG'
# new_image01_png_path = dir + '/new_01.PNG'
# img01.save(new_image01_path)
# img01.save(new_image01_png_path)
# Close file
# img01.close()
