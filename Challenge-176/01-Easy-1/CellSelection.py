import re

def lettersToInt(letters):
	letterval = 0
	for char in letters:
		letterval *= 26
		letterval += ord(char) - ord('A') + 1
	return letterval-1

def coord_to_xy(coordinates):
	letters, numbers = re.split(r'(\d+)', coordinates)[0:2]
	x = int(lettersToInt(letters))
	y = int(numbers)-1 #so that the numbers start at 0 too
	return x, y

def coordinates(current_set):
	this_range = []
	for part in current_set:
		if ':' in part:
			a, b = part.split(':')
			xa, ya = coord_to_xy(a)
			xb, yb = coord_to_xy(b)
			for x in range(xa, xb+1):
				for y in range(ya, yb+1):
					this_range.append((x, y))
		else:
			this_range.append(coord_to_xy(part))
	return this_range

def parse(selection_str):
	include = [selection_str]
	exclude = []
	if '~' in selection_str:
		include = [selection_str.split('~')[0]]
		exclude = [selection_str.split('~')[1]]
	for part in include:
		if '&' in part:
			del include[include.index(part)]
			include += part.split('&')
	for part in exclude:
		if '&' in part:
			del exclude[exclude.index(part)]
			exclude += part.split('&')
	return include, exclude

selection_str = input('Enter your selection string: ')

include, exclude = parse(selection_str)
coord_list = [x for x in coordinates(include) if x not in coordinates(exclude)]
print(len(coord_list))
for coord in coord_list:
	print(coord)
