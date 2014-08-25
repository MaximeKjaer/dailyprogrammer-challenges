def quick_sort(partition):
	if len(partition)<=1:
		return partition
	s, g = [], []
	pivot = partition[0]
	for number in partition[1:]:
		if number < pivot:
			s.append(number)
		else:
			g.append(number)
	return quick_sort(s) + [pivot] + quick_sort(g)

def num(number):
	return float(number) if '.' in number or 'e' in number.lower() else int(number)

n = int(input('How many numbers would you like to sort? '))
partition = [num(input('Enter a number: ')) for i in range(n)]

print(partition)
print(quick_sort(partition))