import random

def bogosort(n, m):
	i = 0
	while n != m:
		n = ''.join(random.sample(n,len(n)))
		i += 1
	print('Finished: %d iterations with word %r' % (i, m))
	return i

def bogobogosort(n, m):
	i = 0 #number of iterations
	j = 2 #number of elements
	while n[:j] != m:
		n = ''.join(random.sample(n,len(n)))
		while n[:j] != m[:j]:
			n = ''.join(random.sample(n,len(n)))
			i += 1
			if n[:j] != m[:j]:
				j = 2 #Start over
		j += 1
	print(i, 'iterations')
	return i

print("BOGO SORT\n==============================")
for i in range(10):
	bogosort("lolhe","hello")

print("\nBOGOBOGO SORT\n==============================")
for i in range(10):
	bogobogosort("lolhe","hello")