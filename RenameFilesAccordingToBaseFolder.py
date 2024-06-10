import pathlib 
import sys
import re
import os

def GetFiles(dir):
    files = []
    for item in os.listdir(dir):
        item_path = os.path.join(dir, item)

        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Recursively traverse the subdirectory and extend the list of files
            files.extend(GetFiles(item_path))
        else:
            # Add the file path to the list
            files.append(item_path)
    return files

def RenameFilesCorrectly(files,basename):
    for currentFilePath in files:
        if not os.path.isdir(currentFilePath) and not currentFilePath.endswith('.meta'):
            splitname = os.path.basename(currentFilePath).split('.')
            filename = splitname[0]
            extension = splitname[1]
            checkFileBase = os.path.basename(filename).split('_')
            dir = os.path.dirname(currentFilePath)
            
            filebasemissmatch = True
            baselist = []
            for base in checkFileBase:
                baselist.append(base) 
                if "_".join(baselist) == basename:
                    filebasemissmatch = False
                    break
                
                
            if filebasemissmatch:
                file_base = filename.split('_')[0]
                newfilename = filename.replace(file_base,basename) + "." + extension
                newfilePath = os.path.join(dir,newfilename)
                if not os.path.isfile(newfilePath):
                     os.rename(currentFilePath,newfilePath)
                     print(f"creating new file path : {newfilePath}")
            else:
                print(f"basename correct for file {currentFilePath}")

if __name__ == "__main__":
    
    #swap out path within the quotes
    baseFolder = r"C:\Users\uttka\unity_work\StudyCrafter_Ghost\MadSci\Assets\CharacterCreator\Character Body Parts\FemaleTeen"

    
    files = GetFiles(baseFolder)
    basename = os.path.basename(baseFolder)
    RenameFilesCorrectly(files, basename)