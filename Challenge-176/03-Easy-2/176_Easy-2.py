def table(farm):
	days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	print('Mill     ' + (' '*8).join(days) + '\n' + '='*80)  #Print the header
	for mill, production in farm:
		print(mill, ' | ', end='')
		for day in days:
			today = str(production[day]) + ' kWh'
			print(today + ' '*(11-len(today)), end='')
		print()

def parse(data):
	farm = {}
	for line in raw_data:
		mill, day, prod = line.split()
		farm[mill] = dict(farm.get(mill, {}), **{day: farm.get(mill, {}).get(day, 0) + int(prod)})  #merge and add
	return (sorted(farm.items()))

with open('windfarm.dat', 'r') as f:
	raw_data = f.readlines()
table(parse(raw_data))