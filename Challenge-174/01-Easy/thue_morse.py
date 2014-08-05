rank = int(input('What rank would you like to calculate Thue-Morse\'s sequence to? ')) + 1
print('nth     Sequence')
print('===========================================================================')

def thue_morse(previous):
	for bit in previous:
		if bit=='0':
			yield '01'
		elif bit=='1':
			yield '10'

for i in range(rank):
	if i == 0:
		current_thue_morse = '0'
	else:
		current_thue_morse = ''.join(thue_morse(current_thue_morse))
	print(i , '     ', current_thue_morse)
