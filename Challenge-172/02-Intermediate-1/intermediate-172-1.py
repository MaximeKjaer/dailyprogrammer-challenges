from __future__ import division
from PIL import Image

pbmFile = raw_input('What file would you like to load? (*.pbm): ')
with open(pbmFile) as f:
        pbm = f.read()

#Let's get rid of comments and extra spaces
pbm = ' '.join([line for line in pbm.split('\n') if '#' not in line])
pbm = ' '.join(pbm.split())
pbm = pbm.strip().split(' ')
#This will work even if it isn't formatted correctly (i.e. there are no newlines)

#Reading the headers
pbmType = pbm[0]
width = int(pbm[1])
height = int(pbm[2])
print 'Type: ', pbmType
print width, 'x', height, 'pixels'
del pbm[0:3]


if pbmType=='P1':
        #Printing an image
        pbm = [pbm[i:i+width] for i in range(0, len(pbm), width)]
        img = Image.new( 'RGB', (width, height), "black")
        pixels = img.load()
        for i in range(width):
                for j in range(height):
                        if int(pbm[j][i])==1:
                                color=(0,0,0)
                        else:
                                color=(255,255,255)
                        pixels[i,j] = color
        img.show()


elif pbmType=='P2':
        maximum = int(pbm[0])
        del pbm[0]
        pbm = [pbm[i:i+width] for i in range(0, len(pbm), width)]
        img = Image.new( 'RGB', (width, height), "black")
        pixels = img.load()
        for i in range(width):
                for j in range(height):
                        color = int(round((int(pbm[j][i])/maximum)*255))
                        pixels[i,j] = (color, color, color)
        img.show()

elif pbmType=='P3':
        maximum = int(pbm[0])
        del pbm[0]
        pbm = [pbm[i:i+3] for i in range(0, len(pbm), 3)]
        pbm = [pbm[i:i+width] for i in range(0, len(pbm), width)]
        img = Image.new( 'RGB', (width, height), "black")
        pixels = img.load()
        print pbm
        for i in range(width):
                for j in range(height):
                        color = (int(pbm[j][i][0]), int(pbm[j][i][1]), int(pbm[j][i][2]))
                        pixels[i,j] = color

        img.show()
else:
        print 'ERROR: Type not recognized.'
