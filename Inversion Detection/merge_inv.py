''' running an inversion detector in a text file'''
from os import sys

def sort_and_count(A):
	n = len(A)
	if n<=1:
		return (A, 0)
		
	else:
		(L, X) = sort_and_count(A[:int(n/2)]) # left
		(R, Y) = sort_and_count(A[int(n/2):]) # right
		(S, Z) = count_split_inv(L,R) # sorted and counted
		return (S, X+Y+Z)
		


def count_split_inv(L,R):
	i, j = 0, 0
	count = 0
	merged = []
	while i<len(L) and j<len(R):
		if L[i] < R[j]:
			merged.append(L[i])
			i+=1
		elif R[j] < L[i]:
			merged.append(R[j])
			j+=1
			count = count + len(L[i:])
	
	if i<len(L):
		merged = merged + L[i:]
	elif j<len(R):
		merged = merged + R[j:]
		
	return (merged, count)
	
	
if __name__ == '__main__':
	with open((sys.argv[1]),'r') as f:
		arr = [int(x.strip('\n')) for x in f]
		(sorted, count) = sort_and_count(arr)
		print(sorted)
		print(count)
		

	
