import os
import pandas as pd

root_dir = 'path'

data = []
for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.png'): # change for your file extension
            file_path = os.path.join(subdir, file)
            label_i = ''
            label_n = ''
            if 'a' in subdir:
                label_i = 'a'
            elif 'b' in subdir:
                label_i = 'b'
            if 'c' in subdir:
                label_n = 'c'
            elif 'd' in subdir:
                label_n = 'd'
            elif 'e' in subdir:
                label_n = 'e'
            elif 'f' in subdir:
                label_n = 'f'
            data.append([file_path, label_i, label_n])
            
df = pd.DataFrame(data, columns=['file_path', 'label_i', 'label_n'])
df.to_csv('dataset.csv', index=False)

print(f'dataset path: {os.getcwd()}')
 