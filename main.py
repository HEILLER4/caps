from scripts.nanodet import NanoDet
from scripts.zoe import ZoeDepth
from scripts.lotus import LotusDepth
from scripts.speech import SpeechHandler
from scripts.ocr import OCRProcessor

# Initialize models
nanodet = NanoDet("models/nanodet.pth")
zoedepth = ZoeDepth("models/zoedepth.pth")
lotus_depth = LotusDepth("models/lotus.pth")
speech = SpeechHandler("models/vosk-model")
ocr = OCRProcessor()

# Simulated detection process
detections = nanodet.detect_objects("data/test_image.jpg")
if detections and detections[0]["distance"] < 5:
    print("Object detected within 5m. Running depth estimation...")
    depth_map = zoedepth.estimate_depth("data/test_image.jpg")

# Speech recognition and OCR
speech_text = speech.recognize_speech()
extracted_text = ocr.extract_text("data/test_image.jpg")
