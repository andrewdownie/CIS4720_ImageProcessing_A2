#http://stackoverflow.com/questions/8849869/how-do-i-find-wally-with-python
import sys
from pprint import pprint
from pylab import imshow, show
import numpy as np
import mahotas
wally = mahotas.imread('images/smooth.jpg')

wfloat = wally.astype(float)
r,g,b = wfloat.transpose((2,0,1))



colCount = int(wally.shape[0])
rowCount = int(wally.shape[1])

img_r = np.zeros((colCount, rowCount))
img_g = np.zeros((colCount, rowCount))
img_b = np.zeros((colCount, rowCount))


for col in range(colCount):
    for row in range(rowCount):
        
        if(r[col, row] > 150 and g[col, row] < 150 and b[col, row] < 150):
            r[col, row] = 255
            g[col, row] = 0
            b[col, row] = 0
        elif (r[col, row] > 150 and g[col, row] > 150 and b[col, row] > 150):
            r[col, row] = 255
            g[col, row] = 255
            b[col, row] = 255
        else:
            r[col, row] = 0 
            g[col, row] = 0 
            b[col, row] = 0 
#        if(r[col, row] )
#        r, g, b = yuv2rgb(img_y[col, row], img_u[col, row], img_v[col, row]) 
#        img_r[col, row] = r
#        img_g[col, row] = g
#        img_b[col, row] = b
            
wally = np.zeros((img_r.shape[0],img_r.shape[1],3), 'uint8')
wally[..., 0] = r
wally[..., 1] = g
wally[..., 2] = b

imshow(wally)
show()
sys.exit()

w = wfloat.mean(2)

pattern = np.ones((32,24), float)

for i in xrange(2):
    pattern[i::8] = -1


v = mahotas.convolve(r-w, pattern)

mask = (v == v.max())
#mask = (v >= v.max())
mask = mahotas.dilate(mask, np.ones((32, 16)))
#pprint(mask)

wally -= (.8*wally * ~mask[:,:,None]).astype('uint8')
imshow(wally)
show()