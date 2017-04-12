#http://stackoverflow.com/questions/8849869/how-do-i-find-wally-with-python
import sys
from pprint import pprint
from pylab import imshow, show
import numpy as np
import mahotas
wally = mahotas.imread('images/wheresWaldo2.jpg')

wfloat = wally.astype(float)
r,g,b = wfloat.transpose((2,0,1))



colCount = int(wally.shape[0])
rowCount = int(wally.shape[1])

img_r = np.zeros((colCount, rowCount))
img_g = np.zeros((colCount, rowCount))
img_b = np.zeros((colCount, rowCount))




for col in range(colCount):
    for row in range(rowCount):
        
        if(r[col, row] > 210 and g[col, row] < 140 and b[col, row] < 140):
            r[col, row] = 255
            g[col, row] = 0
            b[col, row] = 0

for col in range(colCount):
    for row in range(rowCount):
        
        if(r[col, row] == 255 and g[col, row] == 0 and b[col, row] == 0):
            continue
        elif(r[col, row] > 230 and g[col, row] > 230 and b[col, row] > 120):
            r[col, row] = 255
            g[col, row] = 255 
            b[col, row] = 255 
        else:
            r[col, row] = 0
            g[col, row] = 0
            b[col, row] = 0


#turn nearby blacks into reds
for col in range(1, colCount - 1):
    for row in range(1, rowCount - 1):
        
        if(r[col, row] == 255 and g[col, row] == 0 and b[col, row] == 0):
            if(r[col, row + 1] == 0):
                r[col, row] = 255
                g[col, row] = 0
                b[col, row] = 0
            if(r[col + 1, row + 1] == 0):
                r[col, row] = 255
                g[col, row] = 0
                b[col, row] = 0
            if(r[col + 1, row] == 0):
                r[col, row] = 255
                g[col, row] = 0
                b[col, row] = 0
            if(r[col + 1, row - 1] == 0):
                r[col, row] = 255
                g[col, row] = 0
                b[col, row] = 0
            if(r[col, row - 1] == 0):
                r[col, row] = 255
                g[col, row] = 0
                b[col, row] = 0
            if(r[col - 1, row - 1] == 0):
                r[col, row] = 255
                g[col, row] = 0
                b[col, row] = 0
            if(r[col - 1, row] == 0):
                r[col, row] = 255
                g[col, row] = 0
                b[col, row] = 0
            if(r[col - 1, row + 1] == 0):
                r[col, row] = 255
                g[col, row] = 0
                b[col, row] = 0

#turn all blacks into reds
for col in range(1, colCount - 1):
    for row in range(1, rowCount - 1):
        
        if(r[col, row] == 0 and g[col, row] == 0 and b[col, row] == 0):
            r[col, row] = 255

#turn surrounded reds into whites 
for col in range(1, colCount - 1):
    for row in range(1, rowCount - 1):
        redCount = 0
        
        if(r[col, row] == 255 and g[col, row] == 0 and b[col, row] == 0):
            if(r[col, row + 1] == 0 and b[col, row + 1] == 0):
                redCount += 1
            if(r[col + 1, row + 1] == 0 and b[col + 1, row + 1] == 0):
                redCount += 1
            if(r[col + 1, row] == 0 and b[col + 1, row] == 0):
                redCount += 1
            if(r[col + 1, row - 1] == 0 and b[col + 1, row - 1] == 0):
                redCount += 1
            if(r[col, row - 1] == 0 and b[col, row - 1] == 0):
                redCount += 1
            if(r[col - 1, row - 1] == 0 and b[col - 1, row - 1] == 0):
                redCount += 1
            if(r[col - 1, row] == 0 and b[col - 1, row] == 0):
                redCount += 1
            if(r[col - 1, row + 1] == 0 and r[col - 1, row + 1] == 0):
                redCount += 1

            if(redCount >= 7):
                r[col, row] = 255
                b[col, row] = 255
                g[col, row] = 255 

#turn surrounded reds into whites 
for col in range(1, colCount - 1):
    for row in range(1, rowCount - 1):
        whiteCount = 0
        
        if(r[col, row] == 255 and g[col, row] == 0 and b[col, row] == 0):
            if(b[col, row + 1] == 255):
                whiteCount += 1
            if(b[col + 1, row + 1] == 255):
                whiteCount += 1
            if(b[col + 1, row] == 255):
                whiteCount += 1
            if(b[col + 1, row - 1] == 255):
                whiteCount += 1
            if(b[col, row - 1] == 255):
                whiteCount += 1
            if(b[col - 1, row - 1] == 255):
                whiteCount += 1
            if(b[col - 1, row] == 255):
                whiteCount += 1
            if(b[col - 1, row + 1] == 255):
                whiteCount += 1

            if(whiteCount >= 7):
                r[col, row] = 255
                b[col, row] = 255
                g[col, row] = 255 

            

wally = np.zeros((img_r.shape[0],img_r.shape[1],3), 'uint8')
wally[..., 0] = r
wally[..., 1] = g
wally[..., 2] = b

#imshow(wally)
#show()
#sys.exit()

w = wfloat.mean(2)

pattern = np.ones((32,24), float)

for i in xrange(2):
    pattern[i::6] = -1


v = mahotas.convolve(r-w, pattern)

mask = (v == v.max())
#mask = (v >= v.max())
mask = mahotas.dilate(mask, np.ones((32, 16)))
#pprint(mask)

wally -= (.8*wally * ~mask[:,:,None]).astype('uint8')
imshow(wally)
show()