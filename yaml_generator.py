import yaml

with open('C:/Users/HNU/Documents/github/ObjectDetection_Flutter/datasets/data.yaml', 'r') as f:
    data = yaml.load(f)

print(data)

data['train'] = 'C:/Users/HNU/Documents/github/ObjectDetection_Flutter/datasets/train.txt'
data['valid'] = 'C:/Users/HNU/Documents/github/ObjectDetection_Flutter/datasets/valid.txt'

with open('C:/Users/HNU/Documents/github/ObjectDetection_Flutter/datasets/data.yaml', 'w') as f:
    yaml.dump(data, f)

print(data)