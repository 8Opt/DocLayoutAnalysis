import layoutparser.ocr as ocr

from dla.tools.base import BaseAgent
from dla.dependencies import is_tesseract_available


class OCRTool(BaseAgent): 
    def __init__(self, config): 
        self.config = config
        self.model = self.set_model()

    def set_model(self):
        if self.config['type'] == 'tesseract' and is_tesseract_available(): 
            model = ocr.TesseractAgent(languages=self.config['language'])
        else: 
            model = None
        return model
    
    def get_model(self):
        return self.config
    
    def detect(self, image):
        result = self.model.detect(image)
        return result