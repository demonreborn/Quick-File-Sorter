import os
from os import path
import shutil
import time
import configparser

# Get saved variables from config file.
config = configparser.ConfigParser() 
configRoot = "C:\\Users\\RCAdmin\Desktop\\My Python Scripts\\config\\config.ini"
config.read(configRoot)
savedSourceFolder = config.get("folderconfig", "savedDefaultLocationPath")
savedOutputFolder = config.get("folderconfig", "savedDefaultTargetOutputPath")

# Font color and bold class.
class color: 
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# Begin Function
def sort_files():
    print("Would you like to update your default folder paths?")
    print("(1) Default Sorting Folder: " + color.GREEN + savedSourceFolder + color.END)
    print("(2) Default Output Folder: " + color.GREEN + savedOutputFolder + color.END)
    updatePaths = input("1 for Sorting path, 2 for Output path. 0 to skip: ")
    if updatePaths == "1":
        newSortPath = input("Please enter the full path to the folder: ")
        # Rebuild Entire Config I guess. :(
        configFile = open(configRoot, "r")
        list_lines = configFile.readlines()
        list_lines[1] = "savedDefaultLocationPath = " + newSortPath + "\n"
        # Read / Then Write
        configFile = open(configRoot, "w")
        configFile.writelines(list_lines)
        configFile.close()
        print("Default path Updated." + "\n")
        time.sleep(3)
        
    if updatePaths == "2":
        newOutputPath = input("Please enter the full path to the folder:")
        # Rebuild Entire Config I guess. :(
        # Rebuild Entire Config I guess. :(
        configFile = open(configRoot, "r")
        list_lines = configFile.readlines()
        list_lines[2] = "savedDefaultTargetOutputPath = " + newOutputPath + "\n"
        # Read / Then Write
        configFile = open(configRoot, "w")
        configFile.writelines(list_lines)
        configFile.close()
        print("Default path Updated." + "\n")
        time.sleep(3)
        

    print("Please Note that you will need to specify the" + color.BOLD + color.RED + " full root path of the folder" + color.END + " you wish to sort.\n" + color.BOLD + "Example: C:/Users/Desktop/MyFolder" + color.END + "\nOtherwise Enter 1 for Default Source Folder.")
    targetFolder = input("Target Folder Path: ") # Get Target Folder Path
    print("\nEnter 1 for Default Target Destination.")
    targetDest = input("Select File Desination: ") # Get Destination Folder Path
    fileType = input("Enter File Extension you want moved. (Example: .mp3): ") # Get File Type to be sorted.

    if targetFolder == "1": # Default folder
        targetFolder = savedSourceFolder

    if targetDest == "1": # Destination Default
        targestDest = savedOutputFolder

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
        print("Invalid File Type Entered.")
        time.sleep(6)
        print ("\n \n \n \n \n \n")
    
    
while True:
    sort_files()
