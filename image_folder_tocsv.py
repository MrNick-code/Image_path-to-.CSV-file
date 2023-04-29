import os
import pandas as pd
from PIL import Image

img_dir = 'path'

labels = ['label i', 'label i+1', 'label n']
data = {'label i': [], 'label i+1': [], 'label n': []}

for subdir in os.listdir(img_dir):
    if os.path.isdir(os.path.join(img_dir, subdir)):
        for file in os.listdir(os.path.join(img_dir, subdir)):
            file_path = os.path.join(img_dir, subdir, file)
            if file.endswith('.png') and os.path.isfile(file_path):
                img = Image.open(file_path)
                data['file_name'].append(file)
                for label in labels:
                    if label in subdir:
                        data[label].append(1)
                    else:
                        data[label].append(0)

df = pd.DataFrame(data=data, columns=['label i', 'label i+1', 'label n'])
df.to_csv('label_dataset.csv', index=False)

print(f'label_dataset.csv path: {os.getcwd()}')
