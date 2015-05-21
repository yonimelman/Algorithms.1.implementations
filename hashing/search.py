
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
	a = [0,1,5,10,22,30]
	print(index_h(a,-2,0,len(a)-1))
	print(index_h(a,4,0,len(a)-1))
	print(index_h(a,1,0,len(a)-1))
	print(index_h(a,23,0,len(a)-1))