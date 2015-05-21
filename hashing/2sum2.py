from os import sys
from time import time


def twosum(numbers):
	arr = numbers[:]
	ts = set()
	ind = 0
	length = len(arr)
	while length > 0:
		x = arr[ind]
		l = index_l(arr,(-10000 - x),0,len(arr)-1)
		print(l)
		h = index_h(arr,(10000 - x),0,len(arr)-1)
		print(h)
		for y in arr[l:h+1]:
			if y != x:
				if x+y <= 10000 and x+y >= -10000:
					ts.add(x+y)
		arr = arr[ind:h+1]
		ind = h 
	
	return len(ts)
			
		
def index_l(numbers,num,l,r):
	if len(numbers[l:r]) <= 1:
		if num <= numbers[l]:
			return l
		else:
			return r
		
	mid = (l+r)//2
	if num > numbers[mid]:
		return index_l(numbers,num,mid,r)
	elif num < numbers[mid]:
		return index_l(numbers,num,l,mid)
	elif num == numbers[mid]:
		return mid
		
def index_h(numbers,num,l,r):
	if len(numbers[l:r]) <= 1:
		if num >= numbers[r]:
			return r
		else:
			return l
		
	mid = (l+r)//2
	if num > numbers[mid]:
		return index_h(numbers,num,mid,r)
	elif num < numbers[mid]:
		return index_h(numbers,num,l,mid)
	elif num == numbers[mid]:
		return mid
		


if __name__ == '__main__':
	t0 = time()
	numbers = set()
	
	with open((sys.argv[1]),'r') as f:
		for row in f:
			row = row.strip('\n')
			numbers.add(int(row))
	numbers = list(numbers)
	numbers.sort()
	print('done reading: ' + str(time()-t0))

	count = twosum(numbers)
			
	
	
	
	print(count)
	print(len(count))
	print('analysis: ' + str(time()-t0))

		