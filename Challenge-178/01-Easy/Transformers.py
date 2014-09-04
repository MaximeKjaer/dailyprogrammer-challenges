import math

def new(x, y):
	return x, y

def translate(a, b):
	return x+a, y+b

def rotate(a, b, c):
	return (round(a + math.cos(-c)*(x-a) - math.sin(-c)*(y-b), 3),
			round(b + math.sin(-c)*(x-a) + math.cos(-c)*(y-b), 3))

def scale(a, b, c):
	return a+(x-a)*c, b+(y-b)*c

def reflect(axis):
	if axis in 'Xx':
		return x, -y
	elif axis in 'Yy':
		return -x, y

X = 'X'
Y = 'Y'

while True:
	command = input('>> ')
	if command.startswith('('):
		command = 'new' + command
	x, y = eval(command)
	print(x, y)