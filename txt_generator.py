import glob

train_dir = f'C:/Users/HNU/Documents/github/ObjectDetection_Flutter/datasets/train/images/*'
valid_dir = f'C:/Users/HNU/Documents/github/ObjectDetection_Flutter/datasets/val/images/*'
train_data = glob.glob(train_dir)
valid_data = glob.glob(valid_dir)

with open('C:/Users/HNU/Documents/github/ObjectDetection_Flutter/datasets/train.txt', 'w') as f:
    f.write('\n'.join(train_data) + "\n")

with open('C:/Users/HNU/Documents/github/ObjectDetection_Flutter/datasets/val.txt', 'w') as f:
    f.write('\n'.join(valid_data) + "\n")

