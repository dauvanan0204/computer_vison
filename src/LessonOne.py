# Import class image
from PIL import Image

# Folder contain image
dir = 'D:/Python/computervision/image/01'

# Image path
image_path = dir + '/1.JPG'
print(image_path)

# Use funtion Image.open()
img01 = Image.open(image_path)
# Show image
img01.show()
# Định dạng ảnh
print("Định dạng ảnh: " , img01.format)
# print size
print("size: ", img01.size)

# Save image and change
# new_image01_path = dir + '/new_01.JPG'
# new_image01_png_path = dir + '/new_01.PNG'
# img01.save(new_image01_path)
# img01.save(new_image01_png_path)
# Close file
img01.close()
