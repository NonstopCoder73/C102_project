import os
import shutil

from_dir = "C:/Users/amart/Downloads"
to_dir = "C:/Users/amart/Downloads/docs"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
    name, extenstion = os.path.splitext(i) #i is each file in downloads

    if extenstion  == "":
        continue
    if extenstion in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + "/" + i
        path2 = to_dir + "/" + "docs"
        path3 = to_dir + "/" + "docs" + "/" + i

        if os.path.exists(path2):
            print("moving " + i + "...................................................................................")
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("moving " + i + "...................................................................................")
            shutil.move(path1,path3)

