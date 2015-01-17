'''Merge Sort'''

def merge_sort(array):
	n = len(array)
	i, j = 0,0
	sorted_array = ()
	if n > 1:
		l_array = merge_sort(array[:int(n/2)])
		r_array = merge_sort(array[int(n/2):])
		while i<len(l_array) and j<len(r_array):
			if l_array[i] < r_array[j]:
				sorted_array = sorted_array + (l_array[i],)
				i+=1
			else:
				sorted_array = sorted_array + (r_array[j],)
				j+=1
		
		if i<len(l_array):
			sorted_array = sorted_array + l_array[i:]
		elif j<len(r_array):
			sorted_array = sorted_array + r_array[j:]
			
		return sorted_array
				
		
	else:
		return array
		

if __name__ == '__main__':
	arr = (5,2,1,7,9,8,3,)
	print(arr)
	sorted = merge_sort(arr)
	print(sorted)
