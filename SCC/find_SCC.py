from os import sys
from stack import stack
import copy


def DFS_Loop1(Grev):
	global t
	t = 0
	#keeping track of explored nodes
	seen = [None]
	seen.extend([False for x in range(1,len(Grev)+1)])
	#keeping track of finishing times
	ftimes = [None]
	ftimes.extend([None for x in range(1,len(Grev)+1)])
	for i in range(len(Grev),0,-1):
		if not(seen[i]):		
			DFS_iter(Grev,i,ftimes,1,seen)

	return ftimes
			
def DFS(graph,i,lst,loop_n,seen):
	global t
	seen[i] = True
	if loop_n == 2:
		lst[i] = s
	
	
	for arc in graph[i]:
		if not(seen[arc]):
			DFS(graph,arc,lst,loop_n,seen)
			
	if loop_n == 1:
		t += 1
		lst[t] = i
	
	return lst
					
def DFS_iter(graph,i,lst,loop_n,seen):
	global t
	seen[i] = True
	stk = stack()
	arcs = dict()
	stk.push(i)
	node = stk.pop()
	while node != None:
		if node not in arcs:
			arcs[node] = graph[node][:]
	
		if len(arcs[node]) > 0:
			arc = arcs[node].pop()
			if not seen[arc]:
				seen[arc] = True
				stk.push(node)
				node = arc

			
		else:
			if loop_n == 1:
				t += 1
				lst[t] = node
				
			elif loop_n == 2:
				lst[node] = s
				
			node = stk.pop()
			
	return lst
				
def DFS_Loop2(G,ftimes):
	global s
	s = None
	#keeping track of explored nodes

	seen = [None]
	seen.extend([False for x in range(1,len(G)+1)])
	
	# defining leaders
	leader = [None]
	leader.extend([None for x in range(1,len(G)+1)])
	
	for i in reversed(ftimes[1:]):
		if not seen[i]:
			s = i
			DFS_iter(G,i,leader,2,seen)
			
	return leader[1:]	
	
def count_SCC(leader):
	scc_num = []
	leader.sort()
	a = leader[0]
	scc_num.append(1)
	
	for i in range(1,len(leader)):
		if leader[i] > a:
			a = leader[i]
			scc_num.append(1)
		else:
			scc_num[-1] += 1

	
	scc_num.sort(reverse = True)
	
	while len(scc_num) < 5:
		scc_num.append(0)
	
	print(scc_num[:5])
			
if __name__ == '__main__':
	G = dict(zip([x for x in range(1,10)],[[] for x in range(1,10)]))

	Grev = copy.deepcopy(G)
	with open((sys.argv[1]),'r') as f:
		for row in f:
			try:
				row = row.strip('\n')
				row = row.strip(' ')
				lst = row.split(' ')
				lst = [int(x) for x in lst]
				G[lst[0]].append(lst[1])
				Grev[lst[1]].append(lst[0])
			except:
				continue
	
	print("# DFS_LOOP1")
	ftimes = DFS_Loop1(Grev)
	print("# DFS_LOOP2")
	leader = DFS_Loop2(G,ftimes)
	del ftimes
	del G
	del Grev
	print(len(leader))
	print("# COUNTING")
	count_SCC(leader)
	

