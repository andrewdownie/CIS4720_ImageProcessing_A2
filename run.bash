#!/bin/bash
#####
#####               Image-name, location and extensions
#####
templateFolderRelPath="templateImages/"
imageToSearch="wheresWaldo5.jpg"
relPath="images/" #relative to the script being run


python a2.py "$templateFolderRelPath" "$relPath$imageToSearch" 

printf "\nrun.bash has finished\n\n"
