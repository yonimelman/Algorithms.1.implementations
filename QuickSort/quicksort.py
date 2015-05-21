''' running QUICK SORT '''

from os import sys


def choose_pivot_first(array, first, last):
	'''returns the index of the first element to serve as pivot'''
	return first
	
def choose_pivot_last(array,first, last):
	'''returns the index of the last element to serve as pivot'''
	return last-1
	
def choose_pivot_median_of_three(array,first,last):
	length = len(array[first:last])
	if length%2 != 0:
		mid = first + length//2
	elif length%2 == 0:
		mid = first + length//2-1
			
	if (array[first] <= array[mid] and array[mid] <= array[last-1]) or (array[last-1] <= array[mid] and array[mid] <= array[first]):
		return mid
	elif (array[mid] <= array[first] and array[first] <= array[last-1]) or (array[last-1] <= array[first] and array[first] <= array[mid]):
		return first
	elif (array[first] <= array[last-1] and array[last-1] <= array[mid]) or (array[mid] <= array[last-1] and array[last-1] <= array[first]):
		return last-1

	
def partition(array, first, last, pivot):
	'''Partitions the array around the pivot'''
	#move pivot to the first entry
	temp = array[first]
	array[first] = array[pivot]
	array[pivot] = temp
	p = array[first]
	#partition
	
	i = first+1
	
	for j in range(first+1 ,last):
		if array[j] > p:
			pass
		elif array[j] < p:
			temp = array[j]
			array[j] = array[i]
			array[i] = temp
			i += 1		
			
	temp = array[i-1]
	array[i-1] = array[first]
	array[first] = temp
	
	return array, i-1
	
	

def quicksort(array, first, last):
	if len(array[first:last]) <= 1:
		return
		
	global comps
	comps = comps + len(array[first:last])-1
	
	pivot = choose_pivot_median_of_three(array, first, last)
	array, p = partition(array, first, last, pivot)
	
	#p is the pivot index after the partition
	quicksort(array, first, p)
	quicksort(array, p+1, last)
	
	return array
	

if __name__ == '__main__':
	with open((sys.argv[1]),'r') as f:
		array = [int(x.strip('\n')) for x in f]

	comps = 0
	array = quicksort(array,0,len(array))
	print(array)
	
	print('The number of comparisons: {0}'.format(comps))