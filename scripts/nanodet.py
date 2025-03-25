import torch
from nanodet.model.arch import build_model
from nanodet.util import load_model_weight

class NanoDet:
    def __init__(self, model_path):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = build_model()
        load_model_weight(self.model, model_path)
        self.model.to(self.device).eval()

    def detect_objects(self, image):
        # Dummy placeholder function
        return [{"class": "obstacle", "distance": 4.8}]  # Simulating object detected within 5m
