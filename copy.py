import shutil
import glob
import os

folder_names1 = ["train", "valid"]
folder_names2 = ["images", "labels"]
change_file_names = [
    "A", "S",
    "B", 
    "C", 
    "D", 
    "F", "O", 
    "G", 
    "H", "U", 
    "I", "J", 
    "K", "V", 
    "Q", 
    "R", 
    "Y", 
    "Z"]
changed_file_names = [
    "CheerUp", "CheerUp",
    "Stop", 
    "ThisMore", 
    "OneMore",
    "Ok", "Ok", 
    "This", 
    "No", "No", 
    "Promise", "Promise", 
    "Victory", "Victory", 
    "Little", 
    "GoodLuck", 
    "Call", 
    "You"]
cnt = 0
for n in range(len(folder_names1)):
    for m in range(len(folder_names2)):
        for k in range(len(change_file_names)):
            origin_dir = f'D:\github\ObjectDetection_Flutter\datasets/{folder_names1[n]}/{folder_names2[m]}'
            copy_dir = f'D:\github\ObjectDetection_Flutter\datasets/{folder_names1[n]}_copy/{folder_names2[m]}'

            origin_data = glob.glob(origin_dir+f"/{change_file_names[k]}*")
            buffer = []
            splited = "_jpg"
            for data in origin_data:
                buf = data.split("_jpg")[1]
                buffer.append(buf)

            for i, path in enumerate(origin_data):
                _, ext = os.path.splitext(path)
                shutil.copy2(f"{_}{ext}", copy_dir+f"/{changed_file_names[k]}{cnt+i}{splited}"+buffer[i])
            cnt += len(origin_data)
        cnt = 0
