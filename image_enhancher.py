from PIL import Image,ImageFilter
from PIL import ImageEnhance
 
im = Image.open('img.jpg')
 

en = ImageEnhance.Color(im)
en = ImageEnhance.Contrast(im)
en = ImageEnhance.Brightness(im)
en = ImageEnhance.Sharpness(im)
en.enhance(1.5).show("enhanced")
