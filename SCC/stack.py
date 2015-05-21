# Stack
class stack():
	def __init__(self):
		self.stack = []
	
	def push(self,item):
		self.stack.append(item)
		
	def pop(self):
		if len(self.stack) > 0:
			return self.stack.pop()
		else:
			return None
			
