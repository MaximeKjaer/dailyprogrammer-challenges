from PIL import Image

instructions = 'LLRR'
colors = [(255, 255, 255), (0, 0, 0), (255, 0, 0), 	(0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (128, 128, 128)]
width = 1000
height = 1000
ant = {
	'position': [500, 500],
	'angle': 0 #up
}
steps = 10000000


instructions = list(instructions)
color_instructions = dict(zip(colors, instructions))
img = Image.new( 'RGB', (width, height), "white")
pixels = img.load()

for step in range(steps):
	x = ant['position'][0]
	y = ant['position'][1]
	pixel_color = pixels[x, y]
	turn = color_instructions[pixel_color]
	#DEFINING TURN ANGLE
	if turn=='L':
		ant['angle'] = ant['angle'] - 90
	elif turn=='R':
		ant['angle'] = ant['angle'] + 90
	if ant['angle']==360:
		ant['angle'] = 0
	elif ant['angle']==-90:
		ant['angle'] = 270
	#DEFINING NEW COLOR
	next_color = colors.index(pixel_color) + 1
	if next_color >= len(color_instructions):
		next_color = 0
	next_color = colors[next_color]
	#COLORING
	pixels[x,y] = next_color
	#MOVING
	if ant['angle']==0: #go up
		y = y-1
	elif ant['angle']==90: #go right
		x = x-1
	elif ant['angle']==180: #go down
		y = y+1
	elif ant['angle']==270: #go left
		x = x+1
	ant['position'] = [x, y]
img.save('Landons_Ant', 'PNG')
