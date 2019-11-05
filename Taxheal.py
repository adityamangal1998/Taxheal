import os
from pdf2image import convert_from_path
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

filename = '7.pdf'                                                                    #give your file name
images = convert_from_path('7.pdf')
base_filename = os.path.splitext(os.path.basename(filename))[0] + '.jpg'              #path to save the image

save_dir = 'C:/Users/aditya/PycharmProjects/untitled/taxheal/'

for page in images:                                                                   #save the image
    page.save(os.path.join(save_dir, base_filename), 'JPEG')
# os.unlink(base_filename)                                                            #delete for image file
path = base_filename
# img = Image.open(path)
# pix = img.load()
# for y in range(img.size[1]):
#     for x in range(img.size[0]):
#         if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
#             pix[x, y] = (0, 0, 0, 255)
#         else:
#             pix[x, y] = (255, 255, 255, 255)
# img.save('temp.jpg')                                                                  #black and white image
text = pytesseract.image_to_string(Image.open(path))
# os.remove(‘temp.jpg’)                                                               #delete for black and white image file
file = open("final1.txt","w")
file.write(text)
file.close()
