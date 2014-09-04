from urllib import request
from lxml import html
from collections import Counter
import re

def fetch_text(url):
	transcript = []
	page = html.fromstring(request.urlopen(url).read())
	#with open('MPHG.html') as f:
	#	page = html.fromstring(f.read())

	titles = [h4.text for h4 in page.xpath('//h4')]
	texts = [pre.text for pre in page.xpath('//pre')]
	for i in range(len(titles)):
		transcript += [(titles[i], texts[i].replace('\r\n', '\n'))]
	return transcript

def parse(transcript):
	parsed = []
	for item in transcript:
		scene, text = item
		lines = []
		text = re.sub(r'\[(.*?)\]|\((.*?)\)', '', text) #remove stuff between [] or ()
		for line in text.split('\n'):
			if line.strip():
				line = line.strip() #strip the string from unnecessary '\n'and '  '
				#Figure out how to add the line (new line or part of last line?)
				first_words = line.split(':')[0]
				if first_words.isupper() or len(lines)==0:
					lines.append(line) #new character speaking
				else:
					lines[-1] += ' ' + line
		for i in range(len(lines)):
			lines[i] = (lines[i].split(':')[0], ':'.join(lines[i].split(':')[1:]).strip()) #separate text from character
		parsed += [(scene, lines)]
	return parsed

def full_movie_parse(transcript):
	parsed = parse(transcript)
	full_movie = []
	for item in parsed:
		scene, text = item
		full_movie += text
	return full_movie

def n_words(text):
	#The text should be in a list, like this. [('Person A', 'Hello!!'), ('Person B', 'Hi!')]
	n = 0
	for line in text:
		n += len([word for word in line[1].split(' ') if word != ''])
	return n

def n_stage_directions(text):
	n = 0
	for line in text:
		n += line[1].count('(') + line[1].count('[')
	return n

def n_forbidden_words(text):
	n = 0
	for line in text:
		n += line[1].count(' it') + line[1].count('It')
	return n

def get_top(score_dict, top=3):
	i = 0
	score_list = sorted(score_dict, key=score_dict.get, reverse=True)
	top_list = []
	last = ''
	for item in score_list:
		top_list.append((item, score_dict[item]))
		if last != score_dict[item]:
			i+=1
		if i==top:
			break
		last = score_dict[item]
	return top_list

def top_words(text, top=3):
	word_list = []
	for line in text:
		line = re.sub(r'\.|\,|\:|\;|\!|\?|\_', '', line[1])
		spoken_words = [word.lower() for word in line.split(' ') if word != '']
		word_list += spoken_words
	word_dict = dict(Counter(word_list))
	return get_top(word_dict, top)

def top_characters_by_words(text):
	characters = {}
	for line in text:
		name, says = line
		characters[name] = characters.get(name, 0) + n_words([line])
	return get_top(characters, len(characters))

def top_characters_by_lines(text):
	characters = {}
	for line in text:
		name, says = line
		characters[name] = characters.get(name, 0) + 1
	return get_top(characters, len(characters))




transcript = fetch_text('http://www.sacred-texts.com/neu/mphg/mphg.htm')
parsed = parse(transcript)
number_of_words_in_scene = {}

##################
#### BY SCENE ####
##################
for scene, text in parsed:
	print(scene, ':')
	n = n_words(text)
	number_of_words_in_scene[scene] = n
	top = top_words(text, 5)
	percent = sum([x[1] for x in top]) / n *100

	print(' Number of words: ', n)
	print(' Top 5 words: ')
	for word, number in top:
		print('    *', word, '(' + str(number), 'times)')
	print(' Top 5 words make up: ', round(percent, 2), '% of that scene')
	print(' List of characters (sorted by # of words spoken): ')
	for character, words in top_characters_by_words(text):
		print('    *', character, '(' + str(words), 'words)')
	print(' List of characters (sorted by # lines spoken): ')
	for character, lines in top_characters_by_lines(text):
		print('    *', character, '(' + str(lines), 'lines)')
	print('='*80)

##################
### ENTIRE FILM ##
##################
full_movie = full_movie_parse(transcript)

number_of_lines = len(full_movie)
number_of_words = n_words(full_movie)
number_of_stagedirs = n_stage_directions(transcript) #transcript still has [] and ()
number_of_characters = len(top_characters_by_lines(full_movie))
character_words = top_characters_by_words(full_movie)
n_lines = dict(top_characters_by_lines(full_movie))
forbidden = n_forbidden_words(full_movie)

print('ANALYSIS OF THE WHOLE MOVIE:')
print(' Number of words:', number_of_words)
print(' Number of lines:', number_of_lines)
print(' Number of stage directions:', number_of_stagedirs)
print(' Number of characters:', number_of_characters)
print(' Characters (sorted by number of words):')
for character, words, in character_words:
	print('    *', character, 'has spoken', words, 'words and', n_lines[character], 'lines (', round(n_lines[character]/number_of_lines *100, 2), '%)')
print(' Top 10 words:')
for word, number in top_words(full_movie, 10):
	print('    *', word, '(' + str(number), 'times)')
print(' Top 3 scenes (sorted by number of words):')
for scene, number in get_top(number_of_words_in_scene, 3):
	print('    *', scene, '(' + str(number), 'words', round(number/number_of_words*100, 2), '%)')
print(' The forbidden word has been spoken', forbidden, 'times')