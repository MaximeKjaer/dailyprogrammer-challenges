import random

def bogosort(n, m):
	i = 0
	while n != m:
		n = ''.join(random.sample(n,len(n)))
		i += 1
	print('Finished: %d iterations with word %r' % (i, m))
	return i

def bogobogosort(x,y):
    z = ''
    i = 0
    j = 2
    while z != y:
        z = ''.join(random.sample(x, j))
        if z == y[:j]:
            #print(z, 'j =', j)
            j+=1
        else:
            #print(z, 'j =', j)
            j=2
        i+=1
    print('Finished: %d iterations with word %r' % (i, z))


print("BOGO SORT\n==============================")
for i in range(10):
	bogosort("lolhe","hello")

print("\nBOGOBOGO SORT\n==============================")
for i in range(10):
	bogobogosort("lolhe","hello")
