#! python
# creates average color swatches for every image in the current working directory

from skimage import io
import sys
import os
from PIL import Image

iteration_count = 0

while True:
        path = os.getcwd()
        d_path = os.path.join(path, "_swatches")
        os.mkdir(d_path) 
        for root, dirs, files in os.walk(path):
            print(f"There are {len(files)} files in this directory\n"+"_"*20)
            for filename in files:
                    names = str(filename).split(".")
                    try:
                        if names[-1] == "png" or names[-1] == "jpg":
                            og_img = str(filename)
                            new_img = names[0] + "_swatch." + names[-1]
                            print(f"The swatch to be created is {new_img}")
                            dest_path = os.path.join(d_path, new_img)
                            myimg = io.imread(og_img)
                            average = myimg.mean(axis=0).mean(axis=0)
                            print(average)
                            img = Image.new('RGB', (200, 200), (round(average[0]), round(average[1]), round(average[2])))
                            img.save(dest_path, quality=100)
                            print(f"source : {filename}")
                            print(f"resized file : {new_img}\n"+"_"*20+"\n")                
                            iteration_count +=1
                    except:
                        pass
        print(f"{iteration_count} average color swatches were created successfully!!!")
        break
