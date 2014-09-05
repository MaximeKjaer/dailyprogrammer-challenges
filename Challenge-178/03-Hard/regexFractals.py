import re
from PIL import Image

n = int(input('How large should the image be? '))
regex = re.compile(input('Enter a regex: '))


bitmap = ['#'] #I add the # because Python interprets [''] as [] (stupid Python.)

while len(bitmap) < n:
	#divide in 4 quadrants:
	tmp = []
	for line in bitmap:
		tmp_line = []
		for obj in line:
			tmp_line += [obj] + [obj] #Duplicate horizontally
		tmp.append(list(tmp_line)) #Duplicate vertically
		tmp.append(list(tmp_line))
	bitmap = list(tmp)
	#Assign quadrant number
	for y in range(len(bitmap)):
		for x in range(len(bitmap)):
			if y%2==0 and x%2!=0:
				bitmap[y][x] += '1'
			elif y%2==0 and x%2==0:
				bitmap[y][x] += '2'
			elif y%2!=0 and x%2==0:
				bitmap[y][x] += '3'
			else:
				bitmap[y][x] += '4'

img = Image.new( 'RGB', (n, n), "white")
pixels = img.load()

for y in range(len(bitmap)):
	for x in range(len(bitmap)):
		match = regex.search(bitmap[y][x])
		if match:
			pixels[x, y] = (0, 0, 0)

img.save('fractal.png', 'PNG')

