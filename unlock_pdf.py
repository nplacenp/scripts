#! python
# unlock all pdf files in a folder
import os
import pikepdf


iteration_count = 0


while True:
    path = input("Where are the pdf files you would like to unlock? (Must be a proper directory):\n")
    if os.path.isdir(path):
        print("Your input is a directory!")
        # path = os.getcwd()
        new_path = os.path.join(path, "unlocked")
        os.mkdir(new_path)
        for root, dirs, files in os.walk(path):
            print(f"There are {len(files)} files in this directory\n"+"_"*20)
            # print(files)
            for filename in files:
                try:
                    name = filename.split(".")
                    if name[-1] == 'pdf':
                        pdf = pikepdf.open(os.path.join(path,filename))
                        pdf.save(os.path.join(new_path,('unlocked_'+filename)))
                        iteration_count +=1
                except:
                    continue
        print(f"{iteration_count-1} pdf files were unlocked successfully!!!")
        break
    else:
        print("You did not enter a valid directory. Please try again.")
        prompt = input("Would you like to continue?\nPress 'q' to quit\n")
        if prompt == "q":
            break
