import easyocr
from src.preprocessing import enhance_image

class OCREngine:
    def __init__(self, use_gpu=False):
        self.reader = easyocr.Reader(["en"], gpu=use_gpu)

    def extract_text(self, img_path):
        processed = enhance_image(img_path) 
        results = self.reader.readtext(processed, detail=0)
        return results
