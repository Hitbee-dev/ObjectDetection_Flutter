import yaml

with open('C:/Users/HNU/Documents/github/ObjectDetection_Flutter/datasets/data.yaml', 'r') as f:
    data = yaml.load(f)

print(data)

data['train'] = 'C:/Users/HNU/Documents/github/ObjectDetection_Flutter/datasets/train.txt'
data['val'] = 'C:/Users/HNU/Documents/github/ObjectDetection_Flutter/datasets/val.txt'

with open('C:/Users/HNU/Documents/github/ObjectDetection_Flutter/datasets/data.yaml', 'w') as f:
    yaml.dump(data, f)

print(data)