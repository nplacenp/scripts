#! python
# resizes all images in current working directory in either 2k or 4k resolution depending on whether 'hd', 'uhd' or both are offered as system argumemnts

import sys
import os
from PIL import Image


iteration_count = 0

quality_dict = {
                "hd": {"resolution" : (1920, 1080), "suffix": "_2k." },
                "hd_4_3": {"resolution" : (2500, 1875), "suffix": "_2k_4_3." },
                "uhd": {"resolution": (3840, 2160), "suffix": "_4k."},
                "uhd_4_3": {"resolution": (5000, 3750), "suffix": "_4k_4_3."}
                }

sys.argv

for i in sys.argv[1:]:
    while True:
            path = os.getcwd()
            d_path = os.path.join(path, quality_dict[i]["suffix"][1:-1])
            os.mkdir(d_path) 
            for root, dirs, files in os.walk(path):
                print(f"There are {len(files)} files in this directory\n"+"_"*20)
                for filename in files:
                        names = str(filename).split(".")
                        try:
                            if names[-1] == "png" or names[-1] == "jpg":
                                print(f"The file to be resized is {str(filename)}")
                                og_img = str(filename)
                                new_img = names[0] + quality_dict[i]["suffix"] + names[-1]

                                dest_path = os.path.join(d_path, new_img)

                                im = Image.open(og_img)
                                rc_img = im.resize(quality_dict[i]["resolution"])

                                rc_img.save(dest_path, quality=100)

                                print(f"source : {filename}")
                                print(f"resized file : {new_img}\n"+"_"*20+"\n")                
                                iteration_count +=1
                        except:
                            pass
            print(f"{iteration_count} files were resized successfully!!!")
            break
