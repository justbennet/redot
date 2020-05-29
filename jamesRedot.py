import datetime
import os
from os import path
import sys
import shutil
import glob
from subprocess import getoutput


# Remove all existing modules that are loaded for the user. This will run the string "module purge" on the shell and put the stdout in the 'cmd' variable'

cmd = getoutput("module purge") 


# Create a backup directory for the exiting user files. 

now = datetime.datetime.now()
newDirName = now.strftime("redot_backup_%Y_%m_%d_%H:%M:%S")
print("Making directory " + newDirName)
os.mkdir(newDirName)


# Move all existing files in home directory into redot_backup

user = os.environ.get("USER")
userDir = ("/home/" + str(user))

if os.path.isdir(userDir) and os.path.isdir(newDirName) :
    # Iterate over all the files in source directory
    for filePath in glob.glob(userDir + '\*'):
        # Move each file to destination Directory
        shutil.move(filePath, newDirName);
else:
    print(newDirName + "directory does not exist")


# Copy the /etc/skel directory into the cleaned out user's home directory

filesTocopy = "/etc/skel"
newUserhome = shutil.copytree(fileTocopy, userDir)

# Create new .ssh directory. How do I get the proper keys? 

os.mkdir(userDir+./ssh) 


