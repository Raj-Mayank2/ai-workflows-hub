from ocr.easyocr_engine import easyocr_extract_text
from ocr.trocr_engine import trocr_extract_text
from ocr.confidence import is_low_quality
from utils.preprocess import preprocess_image

def extract_text(image_path: str) -> str:
    processed_image = preprocess_image(image_path)

    text = easyocr_extract_text(processed_image)

    if is_low_quality(text):
        text = trocr_extract_text(processed_image)

    return text
