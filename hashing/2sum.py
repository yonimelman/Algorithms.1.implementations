from os import sys
from time import time


def twosum(numbers,t):
	for key in numbers:
			if numbers.__contains__(t-key):
				if key != t-key:
					return True
	return False
	
	

if __name__ == '__main__':
	t0 = time()
	numbers = set()
	
	with open((sys.argv[1]),'r') as f:
		for row in f:
			row = row.strip('\n')
			numbers.add(int(row))
			
			
	count = 0
	print('reading: ' + str(time()-t0))
	for t in range(-10000,10001):
		if twosum(numbers,t):
			count += 1
	
	print(count)
	print('analysis: ' + str(time()-t0))

		