from PIL import Image
import hashlib

username = 'Maxime'
width = 16
height = 16

#CHOSING A COLOR
alphabet = list('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-_')
points = 256 / len(alphabet)
primary = ( round(alphabet.index(username[0])*points), round(alphabet.index(username[1])*points), round(alphabet.index(username[2])*points) )


hashed_username = hashlib.md5(username.encode('utf-8')).hexdigest()
hex_values = [hashed_username[i:i+2] for i in range(0, len(hashed_username), 2)]
binary_values = [bin(int(value, 16))[2:].zfill(8) for value in hex_values]

img = Image.new( 'RGB', (width, height), "white")
pixel = img.load()

for y in range(16):
	for x in range(8):
		if binary_values[y][x] == '1':
			pixel[x, y] = primary
			pixel[15-x, y] = primary

img = img.resize((100, 100))
img.save(username + '.png', 'PNG')
