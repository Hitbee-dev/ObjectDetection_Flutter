import glob
import yaml

train_dir = f'D:\github\ObjectDetection_Flutter\datasets/train/images/*'
valid_dir = f'D:\github\ObjectDetection_Flutter\datasets/valid/images/*'
train_data = glob.glob(train_dir)
valid_data = glob.glob(valid_dir)

with open('D:\github\ObjectDetection_Flutter\datasets/train.txt', 'w') as f:
    f.write('\n'.join(train_data) + "\n")

with open('D:\github\ObjectDetection_Flutter\datasets/valid.txt', 'w') as f:
    f.write('\n'.join(valid_data) + "\n")

with open('D:\github\ObjectDetection_Flutter\datasets/data.yaml', 'w') as f:
    data = yaml.load(f)

print(data)

data['train'] = 'D:\github\ObjectDetection_Flutter\datasets/train.txt'
data['valid'] = 'D:\github\ObjectDetection_Flutter\datasets/valid.txt'

with open('D:\github\ObjectDetection_Flutter\datasets/data.yaml', 'w') as f:
    yaml.dump(data, f)

print(data)