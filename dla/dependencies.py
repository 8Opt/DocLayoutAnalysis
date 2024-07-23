from typing import Any, BinaryIO, Dict, List, Optional, Tuple, Union
import sys
import importlib.util

# The package importlib_metadata is in a different place, depending on the python version.
if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata


# ===== Detector =====
def is_detectron2_available() -> Dict[bool, str]: 
    detectron2_available = importlib.util.find_spec("detectron2") is not None
    try:
        detectron2_version = importlib_metadata.version("detectron2")
    except importlib_metadata.PackageNotFoundError:
        detectron2_available = False
    return {'is_available': detectron2_available, 
            'version': detectron2_version}

def is_paddlepaddle_available() -> Dict[bool, str]:
    paddle_available = importlib.util.find_spec("paddle") is not None
    try:
        paddle_version = importlib_metadata.version("paddlepaddle")
    except importlib_metadata.PackageNotFoundError:
        paddle_available = False

    return {'is_available': paddle_available, 
            'version': paddle_version}


# ===== OCR =====
def is_tesseract_available() -> Dict[bool, str]: 
    pytesseract_available = importlib.util.find_spec("pytesseract") is not None
    try:
        pytesseract_version = importlib_metadata.version("pytesseract")
    except importlib_metadata.PackageNotFoundError:
        pytesseract_available = False

    return {'is_available': pytesseract_available, 
            'version': pytesseract_version}