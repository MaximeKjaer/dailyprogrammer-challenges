import re

cells = {}

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
	try:  #returns selection str if it's an integer; returns the coordinate if the string is a cell (A38, for instance)
		test = float(selection_str)
		return [str(selection_str)]
	except ValueError:
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
		coord_list = [x for x in coordinates(include) if x not in coordinates(exclude)]
		return coord_list

def calculate(formula):
	operands = '+-*/^'
	functions = ['average']
	formula = formula.replace('pi', '3.14159265')
	formula = formula.replace('tau', '6.28318530')
	formula = re.split('(\*|\+|\-|\/|\^)', formula)
	while re.match('[a-zA-Z]', ''.join(formula)):
		formula = ''.join(formula)
		formula = re.split('(\*|\+|\-|\/|\^)', formula)
		for part in formula:
			####### AVERAGE #######
			if part.startswith('average('):
				pattern = re.compile(r'average\((.+?)\)', flags=re.DOTALL)
				results = parse(pattern.findall(part)[0])
				average = sum([float(calculate(cells.get(value, '0'))) for value in results]) / len(results)
				i = formula.index(part)
				formula[i] = str(average)
				part = str(average)
			####### SUM #######
			elif part.startswith('sum('):
				pattern = re.compile(r'sum\((.+?)\)', flags=re.DOTALL)
				results = parse(pattern.findall(part)[0])
				summed = sum([calculate(cells.get(value, '0')) for value in results])
				i = formula.index(part)
				formula[i] = str(summed)
				part = str(summed)
			###### LOGIC ######
			if part not in operands:
				i = formula.index(part)
				value = parse(part)[0]
				if type(value) is tuple:
					formula[i] = calculate(cells.get(value, '0'))
				else:
					formula[i] = value
	formula = ''.join(formula)
	formula = formula.replace('^', '**')  #For eval, cause Python's ^ is **
	formula = eval(formula)  #don't do eval, kids, m'kaaay?
	return str(formula)

def execute(command):
	if '=' in command: #If it's an assignment
		left, right = command.split('=')
		left = parse(left)
		for cell in left:
			cells[cell] = right
	else: #We just want to print a value
		coordinates = parse(command)
		for coordinate in coordinates:
			print(calculate(cells.get(coordinate, '0')))

while True:
	execute(input('>> '))
