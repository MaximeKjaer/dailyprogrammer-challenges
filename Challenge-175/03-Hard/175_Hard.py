from PIL import Image, ImageDraw, ImageOps
from random import randint
from math import sqrt
from shapely.geometry import LineString, mapping

def automatic_mirrors():
	n = 400
	mirrors = []
	for i in range(n):
		x1 = randint(0, 975)
		y1 = randint(0, 975)
		x2 = randint(x1+1, x1+25)
		y2 = randint(y1+1, y1+25)
		mirrors.append({'X1': x1, 'Y1': y1,	'X2': x2, 'Y2': y2})
	mirrors.append({'X1': 0, 'Y1': 999,	'X2': 999, 'Y2': 999}) #top
	mirrors.append({'X1': 998, 'Y1': 998,	'X2': 998, 'Y2': 0}) #right
	mirrors.append({'X1': 0, 'Y1': 0,	'X2': 999, 'Y2': 0}) #bottom
	mirrors.append({'X1': 0, 'Y1': 998,	'X2': 0, 'Y2': 0}) #left
	return mirrors

def automatic_ray():
	ray = {'start': (10, 500),
	   	   'vector': (1, -1),
	   	   'distance': 50000}
	return ray

def normalize(vector): #stolen from /u/lukz
	u, v = vector[0], vector[1]
	s=sqrt(u*u+v*v)
	return (u/s, v/s)

def dot(a, b): #Works for 3D vectors as well
	return a[0]*b[0] + a[1]*b[1]

def reflection(laser, mirror):
	normal = (-mirror[1], mirror[0])
	if dot(laser, normal) < 0:
		normal = (-mirror[1], mirror[0])
	normal = normalize(normal)
	reflected_ray = (-(2*dot(normal, laser)*normal[0]-laser[0]), -(2*dot(normal, laser)*normal[1]-laser[1]))
	return reflected_ray

#Generate mirrors (choose between automatic and manual)
mirrors = automatic_mirrors()
#Load laser (choose between automatic and manual)
ray = automatic_ray()

#Initialize image
img = Image.new( 'RGB', (1000, 1000), "white")
pixels = img.load()
draw = ImageDraw.Draw(img)
draw.ellipse((ray['start'][0]-4, ray['start'][1]-4, ray['start'][0]+4, ray['start'][1]+4), fill='green')

#Draw mirrors
for mirror in mirrors:
	draw.line((mirror['X1'], mirror['Y1'], mirror['X2'], mirror['Y2']), fill='black')

#Setting up the laser
max_distance = ray['distance']
current_distance = 0
min_length = 1500
start = ray['start']
vector = ray['vector']

while current_distance < max_distance:
	laser = LineString([start, (start[0]+vector[0]*1500, start[1]+vector[1]*1500) ])
	#Selecting closest matching mirror (the closest mirror in our path will be the one reflecting the laser).
	for mirror in mirrors:
		x1, y1, x2, y2 = mirror['X1'], mirror['Y1'], mirror['X2'], mirror['Y2']
		mirror = LineString([(x1, y1), (x2, y2)])
		if str(laser.intersection(mirror)) != 'GEOMETRYCOLLECTION EMPTY':
			intersection = laser.intersection(mirror)
			length = LineString([start, mapping(intersection)['coordinates'] ]).length
			if length < min_length and length!=0:
				min_length = length
				mirror_vector = (x2-x1, y2-y1)
				laser_on_glass = mapping(intersection)['coordinates']

	current_distance += length
	if current_distance > max_distance:
		remaining = max_distance - current_distance
		vector = normalize(vector)
		laser_on_glass = (start[0] + vector[0]*remaining, start[1] + vector[1]*remaining)


	#Drawing the correct laser path
	draw.line([start, laser_on_glass], fill='red')
	reflected = reflection(vector, mirror_vector)

	#Preparing for next iteration
	start = laser_on_glass
	vector = reflected
	min_length = 1500

	#This block is used to draw the normal vector to the mirror (for testing purposes):
	#I've commented it out for prettier results.
	#normal = (-mirror_vector[1], mirror_vector[0])
	#draw.line([laser_on_glass, (laser_on_glass[0]+normal[0], laser_on_glass[1]+normal[1])], fill='green')
print(laser_on_glass)
#Draw the final point
draw.ellipse((laser_on_glass[0]-4, laser_on_glass[1]-4, laser_on_glass[0]+4, laser_on_glass[1]+4), fill='red')
#Save.
img = ImageOps.flip(img)
img.save('mirrors_test.png', 'PNG')
