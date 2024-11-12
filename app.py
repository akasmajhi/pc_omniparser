# 1. Import libraries

from ../OmniParser/utils import get_som_labeled_img, check_ocr_box, get_caption_model_processor, get_yolo_model
import torch
from ultralytics import YOLO
from PIL import Image
import base64
import matplotlib.pyplot as plt
import io
import json
from rich import print

# 2. Configuration

# device = 'cuda'
device = 'cpu'
som_model = get_yolo_model(model_path='../OmniParser/weights/icon_detect/best.pt')
som_model.to(device)
print('model to {}'.format(device))
caption_model_processor = get_caption_model_processor(model_name="florence2", model_name_or_path="../OmniParser/weights/icon_caption_florence", device=device)

image_path = '../OmniParser/imgs/windows_multitab.png'
image = Image.open(image_path)
image_rgb = image.convert('RGB')

draw_bbox_config = {
    'text_scale': 0.8,
    'text_thickness': 2,
    'text_padding': 3,
    'thickness': 3,
}
BOX_TRESHOLD = 0.03

# 3. Get labeled image and results
ocr_bbox_rslt, is_goal_filtered = check_ocr_box(
    image_path, 
    display_img=False, 
    output_bb_format='xyxy', 
    goal_filtering=None, 
    easyocr_args={'paragraph': False, 'text_threshold': 0.9}
)
text, ocr_bbox = ocr_bbox_rslt

dino_labeled_img, label_coordinates, parsed_content_list = get_som_labeled_img(
    image_path, 
    som_model, 
    BOX_TRESHOLD=BOX_TRESHOLD, 
    output_coord_in_ratio=False, 
    ocr_bbox=ocr_bbox, 
    draw_bbox_config=draw_bbox_config, 
    caption_model_processor=caption_model_processor, 
    ocr_text=text, 
    use_local_semantics=True, 
    iou_threshold=0.1
)

decoded_image = Image.open(io.BytesIO(base64.b64decode(dino_labeled_img)))
decoded_image.save("labeled_image_output.png")
print(parsed_content_list)
