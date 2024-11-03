import pytesseract
from PIL import Image

def text_recognition(path_to_image):

    image = Image.open(path_to_image)
    text = pytesseract.image_to_string(image, lang='rus+eng')

    strings = text.splitlines()

    text_list = [x for x in strings if x.strip()]

    text = "\n".join(text_list)

    return text
