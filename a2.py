#####
#####               Standard imports
#####
import glob
import sys
from datetime import date, datetime
import time 

from PIL import Image

#####
#####               Relative imports
#####
thisDir = sys.path[0]
sys.path.append(thisDir + '/lib')

from a2_code import *
import a2_code

from imageIO import *
import imageIO




#####
#####               Get command line args 
#####
templateFolder, imageToSearch = ReadCLArgs(thisDir)

print('\nCommand line arguments:')
print('\ttemplateFolder is: ' + templateFolder)
print('\timageToSearch is: ' + imageToSearch)
print('')

#####
#####               Read the image to search
#####
img_r, img_g, img_b = imageIO.imread_colour(imageToSearch)

#####
##### Open all template images 
#####
image_list = []
for filename in glob.glob(templateFolder + '*.jpg'):
    im=Image.open(filename)
    image_list.append(im)

## Go through each template image
for image in image_list:
    temp_r, temp_g, temp_b = Image_To_RGB(image)




#####
#####               Output the image
#####
#print("\nsaving image...\n")
#imageIO.imwrite_colour(outputImage, new_r, new_g, new_b)
#print("\nDone saving image...\n")
print("Exiting...\n")

                        
