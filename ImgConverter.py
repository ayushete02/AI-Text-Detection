import cv2 
import pytesseract

def ConvertText(Path):
    img = cv2.imread(Path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Adding custom options
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=custom_config)

    print(text)

    return text

