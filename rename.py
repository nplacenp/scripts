#! python
# rename all files in folder
import os
import shutil
import random as r
import datetime

from tkinter import *
from tkinter import filedialog

iteration_count = 0

td = datetime.date.today()

# year = td.strftime("%y")
# month = td.strftime("%m")
# day = td.strftime("%d")

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
        pj = input("What is your project name?")
        date_inquiry = input("Do you want to prefix the files with today's date? (y/n)")
        if date_inquiry.lower() != "y":
            cust_date = input("Would you like the prefix the files with a custom date? (y/n)")
            if cust_date.lower() == "y":
                while True:
                        cd = input("What is the custom date you would like the prefix with?  (yymmdd)")
                        if cd.isnumeric():
                            break
                        else:
                            print("Must be a properly formatted date. Please Try Again!")
                            continue

        # path = os.getcwd()
        for root, dirs, files in os.walk(path):
            print(f"There are {len(files)} files in this directory\n"+"_"*20)
            for filename in files:
                    names = str(filename).split(".")
                    try:
                        if names[-1] != "py" and names[-1] != "dat" and names[-1] != "IndexerVolumeGuid":
                            print(f"The file to be renamed is {names[0]}")
                            print(f"The file extension to keep is {names[-1]}\n")
                            source_path = os.path.join(path, str(filename))
                            if date_inquiry.lower() == "y":
                                dest_path = os.path.join(path, f"{td.strftime('%y%m%d')}_{pj}_{iteration_count+1}.{names[-1]}")
                            elif cust_date.lower() == "y":
                                dest_path = os.path.join(path, f"{cd}_{pj}_{iteration_count+1}.{names[-1]}")
                            else:
                                dest_path = os.path.join(path, f"{pj}_{iteration_count+1}.{names[-1]}")
                            print(f"source : {source_path}")
                            print(f"dest : {dest_path}\n"+"_"*20+"\n")                
                            shutil.move(source_path, dest_path)
                            iteration_count +=1
                    except:
                        pass
        print(f"{iteration_count} files were renamed successfully!!!")
        break
    else:
        print("You did not enter a valid directory. Please try again.")
        prompt = input("Would you like to continue?\nPress 'q' to quit\n")
        if prompt == "q":
            break
