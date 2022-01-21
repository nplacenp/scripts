#! python
# rename all files in folder
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

    Button(base, text="Select a file directory png files to convert to jpg",command=openDir,
    bd=5, bg="black", fg="white", activeforeground="green", activebackground="black", relief=RAISED).pack(pady=35)
    mainloop()

    


    if os.path.isdir(path):
        print("Your input is a directory!")
        d_path = os.path.join(path, "jpg")
        os.mkdir(d_path)
        # path = os.getcwd()
        for root, dirs, files in os.walk(path):
            print(f"There are {len(files)} files in this directory\n"+"_"*20)
            for filename in files:
                    names = str(filename).split(".")
                    if names[-1] == "png":
                        print(f"The png to be converted to jpg is {names[0]}")
                        source_path = os.path.join(path, str(filename))
                        dest_path = os.path.join(d_path, f"{names[0]}.jpg")
                        print(f"source : {source_path}")
                        print(f"dest : {dest_path}\n"+"_"*20+"\n")  


                        img_png = Image.open(source_path)
                        rgb_img_png = img_png.convert('RGB')
                        rgb_img_png.save(dest_path)              
                        # shutil.move(source_path, dest_path)
                        iteration_count +=1
        print(f"{iteration_count} png files were converted successfully!!!")
        break
    else:
        print("You did not enter a valid directory. Please try again.")
        prompt = input("Would you like to continue?\nPress 'q' to quit\n")
        if prompt == "q":
            break
