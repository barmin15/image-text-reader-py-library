# run -- pip install pytesseract Pillow

import pytesseract
from PIL import Image, ImageEnhance, ImageFilter


pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract.exe' # update this path for your computer

def preprocess_image(image_path):

    image = image.convert('L')

    image = image.filter(ImageFilter.SHARPEN) # sharpens image

    enhancer = ImageEnhance.Contrast(image) # creates contrast
    image = enhancer.enhance(2)
    return image

def ocr_image(image_path):

    image = preprocess_image(image_path)

    text = pytesseract.image_to_string(image, lang='eng')
    return text


image_path = 'path_to_your_image.jpg' # update this path for your image
extracted_text = ocr_image(image_path)
print(extracted_text)
