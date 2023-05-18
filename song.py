import os
import random
from playsound import playsound

folder_path = '/home/suvedh/songs'  

files = os.listdir(folder_path)

random.shuffle(files)


for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    absolute_path = os.path.abspath(file_path)
    print(absolute_path)
    playsound(absolute_path)
