#Order is decided by http://en.wikipedia.org/wiki/Letter_frequency
from __future__ import division

dictionary = {
	' ': '1',
	'E': '10',
	'T': '11',
	'A': '100',
	'O': '101',
	'I': '110',
	'N': '111',
	'S': '1000',
	'H': '1010',
	'R': '1011',
	'D': '1100',
	'L': '1101',
	'C': '1110',
	'U': '1111',
	'M': '10000',
	'0': '10100',
	'1': '10101',
	'9': '10110',
	'3': '10111',
	'W': '11000',
	'F': '11010',
	'G': '11011',
	'Y': '11100',
	'P': '11101',
	'B': '11110',
	'V': '11111',
	'K': '100000',
	'J': '101010',
	'X': '101011',
	'Q': '101100',
	'Z': '101101',
	'2': '101110',
	'4': '101111',
	'5': '110000',
	'6': '110100',
	'7': '110101',
	'8': '110110'
}
reversed_dictionary = {v:k for k, v in dictionary.items()}


text = ['REMEMBER TO DRINK YOUR OVALTINE',
		'GIANTS BEAT DODGERS 10 TO 9 AND PLAY TOMORROW AT 1300',
		'SPACE THE FINAL FRONTIER THESE ARE THE VOYAGES OF THE BIT STREAM DAILY PROGRAMMER TO SEEK OUT NEW COMPRESSION']


def encode(string):
	output = '00'.join([dictionary[char.upper()] for char in string])
	return output

def decode(string):
	output = string.replace('001', '#1').split('#')
	output = [reversed_dictionary[char] for char in output]
	return ''.join(output)

def challenge(string):
	print "Read message of", len(string), "Bytes"
	a = encode(string)
	print "Compressing ", len(string)*8, " Bits into ", len(a), " Bits (", 100-len(a)/(len(string)*8)*100.0, "% compression)"
	print "Sending Message."
	print "Decompressing Message into", len(string) ,"Bytes."

	b = decode(a)
	if b==string:
		print "Message Matches!"
	else:
		print "Doesn't match. Light pulses will destroy Universe. 42."
	print ""


for line in text:
	challenge(line)
