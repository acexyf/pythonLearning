from PIL import Image, ImageFilter


im = Image.open('img1.JPG')


box = (100, 100, 500, 500)

region = im.crop(box)

region = region.transpose(Image.ROTATE_90)

im.paste(region, box)

im.save('img2.jpg','jpeg')

