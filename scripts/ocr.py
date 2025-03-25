import pytesseract
import cv2

class OCRProcessor:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    def extract_text(self, image_path):
        image = cv2.imread(image_path)
        text = pytesseract.image_to_string(image)
        return text
