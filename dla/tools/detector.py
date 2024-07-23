import layoutparser as lp

from dla.tools.base import BaseAgent
from dla.dependencies import is_detectron2_available, is_paddlepaddle_available
from dla.utils import str_to_json

class DetectTool(BaseAgent): 
    def __init__(self, config): 
        self.config = config
        self.model = self.set_model()
        
    def set_model(self):
        setting_conf = self.config['settings']

        if self.config['type'] == "detectron2" and is_detectron2_available()['is_available']: 
            # for key, values in setting_conf.items():
            #     print(f"{key}: {values}")
            model = lp.Detectron2LayoutModel(**setting_conf)
        elif self.config['type'] == "paddle" and is_paddlepaddle_available()['is_available']: 
            model = lp.PaddleDetectionLayoutModel(**setting_conf)
        else: 
           model = None
        return model 
    
    def get_model(self):
        return self.config

    def detect(self, image):
        result = self.model.detect(image)
        return result