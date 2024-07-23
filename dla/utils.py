from typing import Dict
from PIL import Image
import requests
import yaml, json
import numpy as np
import layoutparser as lp

# ===== Read/Write File =====
def yaml_load(dir): 
    result = yaml.load(open(dir, 'r'), Loader=yaml.FullLoader)
    return result

def str_to_json(input): 
    res = json.loads(input)
    return res

def check_file_format(filename) -> Dict[bool, str]: 
    ACCEPTED_FORMAT = ["jpg","jpeg","png", "PDF", "pdf"]
    result = {
        'is_available': False, 
        'format': None
    }
    file_format = filename.split(".")[-1]
    if file_format not in ACCEPTED_FORMAT: 
        return result
    result['is_available'] = True
    result['format'] = file_format
    return result

# ===== Process Image ======
def load_image(image_str: str) -> Image.Image:
    if image_str.startswith("http"):
        image = Image.open(requests.get(image_str, stream=True).raw).convert("RGB")
    else:
        image = Image.open(image_str).convert("RGB")

    return image

def pil_to_numpy(image) -> np.array:
    return np.array(image)

def list_to_pil(image) -> Image: 
    if not isinstance(image, np.ndarray): 
        image = np.array(image)
    image = Image.fromarray(image.astype(np.uint8))
    return image

def pdf_to_image(dir, load_images:bool): 
    if ".pdf" in dir: 
        pdf_layout, pdf_images = lp.load_pdf(dir, 
                                             load_images=load_images)
        return (pdf_layout, pdf_images)
    return (None, None)

def crop_image(src, rect: lp.elements.Rectangle): 
    box = (rect.block.x_1, rect.block.y_1, rect.block.x_2, rect.block.y_2)
    res = src.crop(box)
    return res