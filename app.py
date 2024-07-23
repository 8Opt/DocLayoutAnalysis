from dla.pipeline import pipeline_layoutparser
from dla.utils import yaml_load, load_image

config = yaml_load(dir='./config.yaml')
sample = ""
sample = load_image(sample)

if __name__ == "__main__": 
    pipeline_layoutparser(config=config,
                          file_obj=sample)