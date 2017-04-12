#http://stackoverflow.com/questions/8849869/how-do-i-find-wally-with-python
import sys
from pprint import pprint
from pylab import imshow, show
import numpy as np
import mahotas
wally = mahotas.imread('images/wheresWaldo1.jpg')

wfloat = wally.astype(float)
r,g,b = wfloat.transpose((2,0,1))



colCount = int(wally.shape[0])
rowCount = int(wally.shape[1])




#Push 'reddish' colours to 100% red
for col in range(colCount):
    for row in range(rowCount):
        
        if(r[col, row] > 210 and g[col, row] < 140 and b[col, row] < 140):
            r[col, row] = 255
            g[col, row] = 0
            b[col, row] = 0

#Push whitish colours to 100% white, leave 100% red untouched, and push everything else to black
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

wally = np.zeros((r.shape[0],r.shape[1],3), 'uint8')
wally[..., 0] = r
wally[..., 1] = g
wally[..., 2] = b

#imshow(wally)
#show()
#sys.exit()

wfloat = wally.astype(float)
r,g,b = wfloat.transpose((2,0,1))

pattern = np.ones((32,24), float)

for i in xrange(2):
    pattern[i::8] = -1


w = wfloat.mean(2)
v = mahotas.convolve(r - w, pattern)

mask = (v == v.max())
mask = mahotas.dilate(mask, np.ones((10, 20)))

wally -= (.8*wally * ~mask[:,:,None]).astype('uint8')
imshow(wally)
show()