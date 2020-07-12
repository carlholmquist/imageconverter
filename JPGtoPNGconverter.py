import sys
import os
import re
from PIL import Image

path_to_pic = sys.argv[1]
name_new_folder = sys.argv[2]
while True:
    try:
        os.mkdir(name_new_folder)
    except FileExistsError:
        break

images_in_dir = list(filter(lambda var: var[-4:] == '.jpg', os.listdir(path_to_pic)))

for i in images_in_dir:
    input_file = i
    e,f = os.path.splitext(i)
    output_file = e + '.png'
    if input_file != output_file:
        with Image.open(f'{path_to_pic}/{input_file}') as im:
            im.save(f'{name_new_folder}/{output_file}')