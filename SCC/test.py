def t1(lst):
	lst[0]=2
	print(lst)
	return lst
	
def t2(a):
	a[3] = 55
	print(a)
	
lst = [1,0,0,0]
print(lst)

t1(lst)
t2(lst)
print(lst)


	