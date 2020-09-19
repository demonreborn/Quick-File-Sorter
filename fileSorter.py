import os
from os import path
import shutil
import time

def sort_files():
    print("Please Note that you will need to specify the full root path of the folder you wish to sort.\nExample: C:/Users/Desktop/MyFolder\nEnter 1 for Default Source Folder.")
    targetFolder = input("Target Folder Path: ") # Get Target Folder Path
    print("\nEnter 1 for Default Target Destination.")
    targetDest = input("Select File Desination: ") # Get Destination Folder Path
    fileType = input("Enter File Extension you want moved. (Example: .mp3): ") # Get File Type to be sorted.

    if targetFolder == "1": # Default folder
        targetFolder = "C:\\Users\\RCAdmin\\Desktop\\Folder_1\\"

    if targetDest == "1": # Destination Default
        targestDest = "C:\\Users\\RCAdmin\\Desktop\\Folder_2\\"

    if fileType.startswith("."): 
        src = targetFolder
        dst = targestDest
   
        fileList = [m for m in os.listdir(src) if m.endswith(fileType) and path.isfile(path.join(src, m))] # Move Files
        for f in fileList:
            shutil.move(path.join(src, f), dst)
            
        print("\n \n")
        if not fileList:
            print("------------------------------------------------------------------")
            print("The file type:", fileType, "Does not exist in the chosen directory:", targetFolder)
        else:
            print("------------------------------------------------------------------")
            print("Files Moved:", fileList)

        print ("\n \n")
        print("Target Sort Folder:", src)
        print ("Sorted Destination Folder:", dst)
        time.sleep(10)
        print ("\n \n \n \n \n \n")
    
    else:
        print("Invalid File Type.")
        time.sleep(5)
        print ("\n \n \n \n \n \n")
        return False
    
    
while True:
    sort_files()
