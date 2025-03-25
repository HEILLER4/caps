import torch
from ZoeDepth.zoedepth.models.builder import build_model

class ZoeDepth:
    def __init__(self, model_path):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = build_model()
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))
        self.model.to(self.device).eval()

    def estimate_depth(self, image):
        return self.model(image)  # Placeholder for depth estimation output
