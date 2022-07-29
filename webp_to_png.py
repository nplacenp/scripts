#! python
# convert webp images in directory to png format
import os
import shutil

from tkinter import *
from tkinter import filedialog
from PIL import Image

iteration_count = 0

while True:
    path = ""


    def openDir():
        global path
        path = filedialog.askdirectory(initialdir="/")
        base.destroy()

    base = Tk()
    base.geometry("500x150")
    base.configure(background="black")

    Button(base, text="Select a file directory with webp files to convert to png",command=openDir,
    bd=5, bg="black", fg="white", activeforeground="green", activebackground="black", relief=RAISED).pack(pady=35)
    mainloop()

    


    if os.path.isdir(path):
        print("Your input is a directory!")
        d_path = os.path.join(path, "png")
        os.mkdir(d_path)
        # path = os.getcwd()
        for root, dirs, files in os.walk(path):
            print(f"There are {len(files)} files in this directory\n"+"_"*20)
            for filename in files:
                    names = str(filename).split(".")
                    if names[-1] == "webp":
                        print(f"The webp file to be converted to png is {names[0]}")
                        source_path = os.path.join(path, str(filename))
                        dest_path = os.path.join(d_path, f"{names[0]}.png")
                        print(f"source : {source_path}")
                        print(f"dest : {dest_path}\n"+"_"*20+"\n")  


                        img_webp = Image.open(source_path)
                        img_webp.save(dest_path, format="png", lossless=True, quality=100)              
                        iteration_count +=1
        print(f"{iteration_count} webp files were converted successfully!!!")
        break
    else:
        print("You did not enter a valid directory. Please try again.")
        prompt = input("Would you like to continue?\nPress 'q' to quit\n")
        if prompt == "q":
            break
