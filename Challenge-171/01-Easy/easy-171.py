hexvalue = '93 93 93 F3 F3 93 93 93'.split(' ')
binary = [bin(int(line, 16))[2:].zfill(8) for line in hexvalue] #Convert it to a list of binary lines
image = [pixel.replace('1', '*').replace('0', ' ') for pixel in binary] #Convert it to a list of lines
print '\n'.join(image)
