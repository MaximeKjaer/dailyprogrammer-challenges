import wave
import struct
import math

def morse_conversion(message):
	code = ''
	units = 0
	for letter in message.upper():
		code += morse[letter] + '|'
	return code.replace('|/|', '/')

def wav(code):
	frequency = 440 #Hz
	framerate = 10000.00 #Hz
	amp=8000.0 # amplitude
	time_per_unit = 0.125 #seconds

	unit=[]
	for x in range(int(math.ceil(time_per_unit * framerate))): #one full unit consists of time_per_unit*framerate frames
		unit.append(math.sin(2*math.pi * frequency * ( x/framerate)))
	empty = [0]*int(time_per_unit * framerate)

	file_list = []
	for char in code:
		if char == '.':
			for s in unit:
				file_list.append(struct.pack('h', int(s*amp/2)))
		elif char == '-':
			for s in unit*3:
				file_list.append(struct.pack('h', int(s*amp/2)))
		elif char == '|':
			for s in empty:
				file_list.append(struct.pack('h', int(s*amp/2)))
		elif char == '/':
			for s in empty*5: #5, not 7, since I'm adding an empty before and after
				file_list.append(struct.pack('h', int(s*amp/2)))
		for s in empty:
			file_list.append(struct.pack('h', int(s*amp/2)))

	wav_file=wave.open('morse.wav','w')
	wav_file.setparams((1, 2, int(framerate), len(file_list), 'NONE', 'not compressed'))
	print "Writing sines to file..."
	i = 0
	for s in file_list:
		i+=1
		if i % (len(file_list)/4)==0:
			print int(math.ceil((1.0*i/len(file_list))*100)), '%'
		wav_file.writeframes(s)
	wav_file.close()

	
morse = {
	'A': '.-', 'B': '-...',  'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
	'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
	'S': '...',	'T': '-',	'U': '..--',	'V': '...-',	'W': '.--',	'X': '-..-', 'Y': '-.--', 'Z': '--..',
	'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '......', '6': '-....', '7': '--...',
	'8': '---..', '9': '----.', ' ': '/'
}

message = raw_input('Enter a message: ')
print morse_conversion(message)
wav(morse_conversion(message))