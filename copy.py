import shutil
import glob
import os
import re

folder_name1 = "train"
folder_name2 = "images"

origin_dir = f'{os.environ["USERPROFILE"]}/Documents/Dev/{folder_name1}/{folder_name2}'
copy_dir = f'{os.environ["USERPROFILE"]}/Documents/Dev/{folder_name1}_copy/{folder_name2}'

origin_data = glob.glob(origin_dir+"/A*")
buffer = []
splited = "_jpg"
for data in origin_data:
    buf = data.split("_jpg")[1]
    buffer.append(buf)

for i, path in enumerate(origin_data):
    _, ext = os.path.splitext(path)
    shutil.copy2(f"{_}{ext}", copy_dir+f"/A{i}{splited}"+buffer[i])

