from os import sys
from time import time
from math import ceil
import heapq
from pprint import pprint as pp


def heappop_large(h):
	return (heapq.heappop(h))*-1
	
def heap_large(h):
	return (h[0])*-1
	
def heappush_large(h,item):
	heapq.heappush(h,(item)*-1)
	
def sum_medians(medians):
	print('sum of the medians (last 4 digits): ' + str(sum(medians)%10000))
		

if __name__ == '__main__':
	t0 = time()
	numbers = []
	
	with open((sys.argv[1]),'r') as f:
		for row in f:
			row = row.strip('\n')
			numbers.append(int(row))
	
	print('done reading: ' + str(time()-t0))
	
	hlow = []
	hhigh = []
	medians = []
	count = 0
	
	for num in numbers:
		count+=1
		heappush_large(hlow,num)
		
		if len(hlow) > ceil(count/2):
			heapq.heappush(hhigh,heappop_large(hlow))
		
		elif len(hhigh) > 0:
			if heap_large(hlow) > hhigh[0]:
				heappush_large(hlow,heapq.heappop(hhigh))
				heapq.heappush(hhigh,heappop_large(hlow))

		

		#update the median	
		medians.append(heap_large(hlow))
	
	sum_medians(medians)
	
		
	
	print('done analyzing: ' + str(time()-t0))	
		
		
		
	 
	
	
	
	
	
	
			
