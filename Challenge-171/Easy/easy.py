hexvalue = 'FF 81 BD A5 A5 BD 81 FF'.split(' ')
binary = [bin(int(line, 16))[2:] for line in hexvalue] #Convert it to a list of binary lines
image = [pixel.replace('1', '* ').replace('0', '  ') for pixel in binary] #Convert it to a list of lines
print '\n'.join(image) #Print it line by line
