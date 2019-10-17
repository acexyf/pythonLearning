from PIL import Image
import pytesseract
image = Image.open('./timg.jpg')

text = pytesseract.image_to_string(image)
print(text)