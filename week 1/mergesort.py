'''Merge Sort'''

def merge_sort(array):
	n = len(array)
	i, j = 1,1
	sorted_array = []
	if n > 1:
		l_array = merge_sort(array[:int(n/2)])
		r_array = merge_sort(array[int(n/2):])
		while i<len(l_array) or j<len(r_array):
			if l_array[i] < r_array[j]:
				sorted_array.append(l_array[i])
				i+=1
			else:
				sorted_array.append(r_array[j])
				j+=1
		return sorted_array
				
		
	else:
		return array
		







if __name__ == '__main__':
	merge_sort([5,2,1,7,9,8,3,4])