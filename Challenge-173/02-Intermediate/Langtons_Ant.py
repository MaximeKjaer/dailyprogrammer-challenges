from PIL import Image

instructions = 'RRLRLR'
colors = [(255, 255, 255), (0, 0, 0), (255, 0, 0), 	(0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (128, 128, 128)]
movements = [
	[0, -1], #up
	[-1, 0], #right
	[0, 1], #down
	[1, 0] #left
]
width = 1000
height = 1000
ant = {
	'position': [500, 500],
	'angle': 0 #up
}
test_angle = 0
steps = 100000

instructions = list(instructions)
rule = dict(zip(colors, instructions))
img = Image.new( 'RGB', (width, height), "white")
pixels = img.load()

for step in range(steps):
	x = ant['position'][0]
	y = ant['position'][1]
	pixel_color = pixels[x, y]
	turn = rule[pixel_color]
	#DEFINING TURN ANGLE
	if turn=='L':
		ant['angle'] = (ant['angle'] - 1) % 4
	elif turn=='R':
		ant['angle'] = (ant['angle'] + 1) % 4
	#DEFINING THE PIXEL'S NEW COLOR
	next_color = colors.index(pixel_color) + 1
	if next_color >= len(rule):
		next_color = 0
	next_color = colors[next_color]
	#COLORING THE CURRENT PIXEL
	pixels[x,y] = next_color
	#MOVING THE ANT
	ant['position'][0] += movements[ant['angle']][0]
	ant['position'][1] += movements[ant['angle']][1]
img.save('Landons_Ant3', 'PNG')
