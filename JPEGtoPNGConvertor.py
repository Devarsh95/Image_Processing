import sys
import os
from PIL import Image

Input_Image = sys.argv[1]
Output_Image = sys.argv[2]

if not os.path.exists(Output_Image):
    os.makedirs(Output_Image)

for files in os.listdir(Input_Image):
    img = Image.open(f"{Input_Image}{files}")
    clear_ext = os.path.splitext(files)[0]
    img.save(f"{Output_Image}{files}.png", "png")
    print("your image has been processed")
