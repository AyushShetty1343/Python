#6b
import os
import zipfile
def createzip(folderpath,filename):
    try:
        with zipfile.ZipFile(filename,"w") as zfile:
            for root,_,files in os.walk(folderpath):
                for file in files:
                    filepath=os.path.join(root,file)
                    arcname=os.path.relpath(filepath,folderpath)
                    zfile.write(filepath,arcname)
        print(f"ZIP file '{filename}' created successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")
        
if __name__=="__main__":
    folderpath=input("enter folder path to zip: ")
    filename=input("enter name of zip file to be created: ")
    createzip(folderpath,filename)