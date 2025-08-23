new_file = open("new_file.txt", 'x')

new_file.close()

import os 

if os.path.exists("coding.txt"):

    os.remove("coding.txt")

else:
    print("The file doesnt exist.")

os.rmdir("folder")