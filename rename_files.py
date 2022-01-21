#! python
# rename all files in folder
import os
import shutil
import random as r

from tkinter import *
from tkinter import filedialog

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

    Button(base, text="Where are the files you would like to rename?",command=openDir,
    bd=5, bg="black", fg="white", activeforeground="green", activebackground="black", relief=RAISED).pack(pady=35)
    mainloop()


    if os.path.isdir(path):
        print("Your input is a directory!")
        # path = os.getcwd()
        for root, dirs, files in os.walk(path):
            print(f"There are {len(files)} files in this directory\n"+"_"*20)
            for filename in files:
                    names = str(filename).split(".")
                    if names[-1] != "py" and names[-1] != "dat" and names[-1] != "IndexerVolumeGuid":
                        print(f"The file to be renamed is {names[0]}")
                        print(f"The file extension to keep is {names[-1]}\n")
                        source_path = os.path.join(path, str(filename))
                        dest_path = os.path.join(path, f"{r.randint(0,100000000000)}.{names[-1]}")
                        print(f"source : {source_path}")
                        print(f"dest : {dest_path}\n"+"_"*20+"\n")                
                        shutil.move(source_path, dest_path)
                        iteration_count +=1
        print(f"{iteration_count} files were renamed successfully!!!")
        break
    else:
        print("You did not enter a valid directory. Please try again.")
        prompt = input("Would you like to continue?\nPress 'q' to quit\n")
        if prompt == "q":
            break
