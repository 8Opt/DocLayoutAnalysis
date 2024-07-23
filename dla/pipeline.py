from typing import Union
from PIL import Image

import numpy as np
import layoutparser as lp

from dla.utils import check_file_format, pdf_to_image

from dla.tools import DetectTool, OCRTool

def pipeline_layoutparser(config, 
                          file_obj: Union[np.ndarray, Image.Image, str],
                          verbose=False): 

    if isinstance(file_obj, str): 
        file_format = check_file_format(filename=file_obj)
        if file_format == "pdf" or file_format == "PDF": 
            file_obj = pdf_to_image(file_obj)
        else: 
            raise "[Error] Invalid filename or your input file format is not supported"
    else: 
        file_obj = [file_obj]

    detect_tool = DetectTool(config['detector'])
    ocr_tool = OCRTool(config['ocr'])

    n_files = len(file_obj)
    print(f"[Info] Processing {n_files} file(s) ...")

    for idx in range(n_files): 
        sample = file_obj[idx]
        layout = detect_tool.detect(sample)
        text_blocks = lp.Layout([b for b in layout if b.type=='Text'])
        figure_blocks = lp.Layout([b for b in layout if b.type=='Figure'])

        h, w = np.array(sample).shape[:2]

        left_interval = lp.Interval(0, w/2*1.05, axis='x').put_on_canvas(sample)

        left_blocks = text_blocks.filter_by(left_interval, center=True)
        left_blocks = sorted(left_blocks, key = lambda b:b.coordinates[1])

        right_blocks = [b for b in text_blocks if b not in left_blocks]
        right_blocks = sorted(right_blocks, key = lambda b:b.coordinates[1])

        text_blocks = lp.Layout([b.set(id=idx) for idx, b in enumerate(left_blocks+right_blocks)])

        for block in text_blocks:
            segment_image = (block.pad(left=5, right=5, top=5, bottom=5)
                                    .crop_image(np.array(sample)))
                # add padding in each image segment can help
                # improve robustness

            text = ocr_tool.detect(segment_image)
            block.set(text=text, inplace=True)

    idx = 0
    for txt in text_blocks.get_texts():
        print(idx, txt, end='\n---\n')
        idx += 1