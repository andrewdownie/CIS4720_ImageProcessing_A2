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
img_width = img_r.shape[1]
img_height = img_r.shape[0]


#####
##### Open all template images 
#####
image_list = []
for filename in glob.glob(templateFolder + '*.jpg'):
    im=Image.open(filename)
    image_list.append(im)

templateIndex = 0
## Go through each template image
for image in image_list:
    print("Searching for template: " + str(templateIndex))
    templateIndex = templateIndex + 1
    temp_r, temp_g, temp_b = Image_To_RGB(image)
    temp_width = temp_r.shape[1]
    temp_height = temp_r.shape[0]
    print(str(temp_width) + " " + str(temp_height))


    searchWidth = img_width - temp_width
    searchHeight = img_height - temp_height
    
    #Go through every pixel in the source image
    for src_x in range(0, searchWidth - 1):
        for src_y in range(0, searchHeight - 1):
            print(src_y)

            #Go through every pixel in the temp image
            for temp_x in range(0, temp_width - 1):
                for temp_y in range(0, temp_height - 1):
                    if(temp_x >= temp_width - 1 or temp_y >= temp_height - 1):
                        continue 

                    #Compare the source image and the temp image
#                    print(str(temp_r[0, temp_x]))
#                    print(str(temp_r[temp_y, 0]))

                    if(temp_r[temp_y, temp_x] == 255):
                        continue
                    elif(temp_r[temp_y, temp_x] != img_r[temp_y, temp_x]):
#                        temp_x = temp_width
#                        temp_y = temp_height
                        continue
           
    print("image wh: " + str(src_x) + " " + str(src_y))





print("Exiting...\n")

                        
