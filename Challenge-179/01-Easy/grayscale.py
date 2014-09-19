from PIL import Image

def naive(pixel):
	average = round(sum(pixel)/3)
	return (average, average, average)

def lightness(pixel):
	average = round((max(pixel) + min(pixel))/2)
	return (average, average, average)

def luminosity(pixel):
	R, G, B = pixel
	average = round(0.21*R + 0.72*G + 0.07*B)
	return (average, average, average)

filepath = input("Enter the image's filepath: ")
print("1. Naive")
print("2. Lightness")
print("3. Luminosity")
conversion = input("What conversion algorithm would you like to use? [1|2|3] ")

img = Image.open(filepath)
pixels = img.load()
width, height = img.size
for pixel in ((x,y) for x in range(width) for y in range(height)):
	if conversion == "1":
		pixels[pixel] = naive(pixels[pixel])
	elif conversion == "2":
		pixels[pixel] = lightness(pixels[pixel])
	else:
		pixels[pixel] = luminosity(pixels[pixel])
if conversion == "1":
	img.save("naive.PNG", "PNG")
elif conversion == "2":
	img.save("lightness.PNG", "PNG")
else:
	img.save("luminosity.PNG", "PNG")