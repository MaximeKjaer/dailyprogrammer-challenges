#Challenge 171 Intermediate

hexvalue = 'FF 81 BD A5 A5 BD 81 FF'.split(' ')
binary = [bin(int(line, 16))[2:].zfill(8) for line in hexvalue] #Convert it to a list of binary lines
image = [pixel.replace('1', '*').replace('0', ' ') for pixel in binary] #Convert it to a list of lines
print 'ORIGINAL IMAGE'
print '\n'.join(image)


def zoom(image, factor):
	if factor%1==0 and factor>=1:
		return '\n'.join([''.join([str(pixel)*factor for pixel in line]) for line in image for i in range(factor)])
	else:
		a = int(1/factor)
		return '\n'.join([line[::a] for line in image[::a]])

def invert(image):
	return '\n'.join([line.replace('*', '#').replace(' ', '*').replace('#', ' ') for line in image])


def rotate_clockwise(image):
	image = [list(line) for line in image] #We create a pixel matrix
	a = len(image)
	new = [[[] for _ in range(a)] for _ in range(a)]
	for x in range(a):
		for y in range(a):
			new[y][a-1-x] = image[x][y]
	return '\n'.join([''.join(line) for line in new])

def rotate_counter_clockwise(image):
	image = [list(line) for line in image] #We create a pixel matrix
	a = len(image)
	new = [[[] for _ in range(a)] for _ in range(a)]
	for x in range(a):
		for y in range(a):
			new[a-1-y][x] = image[x][y]
	return '\n'.join([''.join(line) for line in new])

def prepare_for_next(image):
	return image.split('\n')

#Now to the actual Challenge:
zoomed = zoom(image, 2)
image = prepare_for_next(zoomed)
rotated = rotate_clockwise(image)
image = prepare_for_next(rotated)
zoomed = zoom(image,2)
image = prepare_for_next(zoomed)
inverted = invert(image)
image = prepare_for_next(inverted)
zoomed_out = zoom(image, 0.5)

print zoomed_out
