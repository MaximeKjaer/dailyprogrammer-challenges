words = 'hello yyyyyyy yzyzyzyzyzyz mellow well yo kellow lellow abcdefhijkl hi is yellow just here to add strings fellow lellow llleow'.split(' ')
letters = 'l e l o h m f y z a b w'.split(' ')
matches = []

for word in words:
	letters_copy = list(letters)
	success = True
	for letter in word:
		success = letter in letters_copy
		if not success:
			break
		del letters_copy[letters_copy.index(letter)]
	if success:
		matches.append(word)

if matches == []:
	print('No Words Found')
else:
	matches.sort(key=len, reverse=True)
	matches = [match for match in matches if len(match) == len(matches[0])]
	print('\n'.join(matches))
