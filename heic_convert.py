#! python
# converts all heic files as file formats offered as system argumemnts (png or jpg)

import sys
import os
from PIL import Image
import pillow_heif


iteration_count = 0

sys.argv

for i in sys.argv[1:]:
    while True:
            path = os.getcwd()
            d_path = os.path.join(path, i)
            try:
                os.mkdir(d_path)
            except:
                pass
            for root, dirs, files in os.walk(path):
                print(f"There are {len(files)} files in this directory\n"+"_"*20)
                for filename in files:
                        names = str(filename).split(".")
                        try:
                            if names[-1] == "HEIC":
                                print(f"The file to be converted is {str(filename)}")
                                og_img = str(filename)
                                new_img = names[0] + "." + i
                                heif_file = pillow_heif.read_heif(filename)
                                image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw")
                                dest_path = os.path.join(d_path, new_img)
                                image.save(dest_path, quality=100)
                                print(f"source : {filename}")
                                print(f"resized file : {new_img}\n"+"_"*20+"\n")                
                                iteration_count +=1
                        except:
                            pass
            print(f"{iteration_count} files were resized successfully!!!")
            break
