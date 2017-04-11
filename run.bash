#!/bin/bash
#####
#####               Image-name, location and extensions
#####
imgName="wheresWaldo2"
relPath="images/" #relative to the script being run
inExt=".jpg"
outExt=".jpg"

#####
#####               The available algorithms to run
#####
morph_toggleCE="morph_toggleCE"
histhyper="histhyper"
morph_CE="morph_CE"
drew_CE="drew_CE"

seperator=" - "

IN_FILE="$relPath$imgName$inExt" 

#####
#####               FUNCTION: RunAlgo, takes the algorithm you want to run as parameter one 
#####
RunAlgo(){
    OUT_FILE="$relPath$imgName$seperator$1$outExt" 
    python a2.py "$IN_FILE" "$OUT_FILE" "$1"
}

#####
#####               Run the algorithms
#####
RunAlgo "$morph_toggleCE"
RunAlgo "$histhyper"
RunAlgo "$morph_CE"
RunAlgo "$drew_CE"

printf "\nrun.bash has finished\n\n"
