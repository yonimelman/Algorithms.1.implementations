from os import sys
from pprint import pprint as pp


def dijkstra(adj,source):
	'''Calculates every short path from source vertex to any other connected vertex
	input: 	adj - adjcency list
			source - the source vertex
			
	output:	A - a list with the distances'''
	
	A = [None]
	A.extend([0 for x in range(1,201)])
	X = []								

	A[source] = 0
	X.append(source)
	
	while X != list(adj.keys()):
		score = 100000
#		edges = [[(item[0],pair) for pair in item[1] if pair[0] not in X] for item in list(adj.items()) if item[0] in X]
		available_edges = [[(item[0],pair[0],pair[1]) for pair in item[1] if pair[0] not in X] for item in list(adj.items()) if item[0] in X]
		edges = []
		for a_edges in available_edges:
			edges.extend(a_edges)
		
		if len(edges) > 0:
			for edge in edges:
				w_temp, score_temp = g_score(A,edge)
				if score_temp < score:
					w = w_temp
					score = score_temp
			
			X.append(w)
			A[w] = score
		else:
			break
	return A
	
	
def g_score(A, edge):
	v = edge[0]
	w = edge[1]
	l = edge[2]

	return (w, A[v] + l)


def s_path_specific(A):
	print((A[7],A[37],A[59],A[82],A[99],A[115],A[133],A[165],A[188],A[197]))



if __name__ == '__main__':
	adj = dict()
	with open((sys.argv[1]),'r') as f:
		for row in f:
			try:
				row = row.strip('\t\n')
				lst = row.split('\t')
				vertex = int(lst[0])
				adj[vertex] = []
				for pair in lst[1:]:
					adj[vertex].append(tuple([int(x) for x in pair.split(',')]))
			except:
				continue
	
	A = dijkstra(adj,1)
	s_path_specific(A)
	