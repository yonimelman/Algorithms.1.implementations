
from os import sys
from pprint import pprint as pp
from random import choice


def graph_create(nodes,edges):
	graph = dict(zip(nodes,edges))
	return graph
	
def graph_remove(graph,node):
	del graph[node]
	return graph
	
def readress_node(graph,node1,node2):
	edges1 = graph.pop(node1)
	edges2 = graph.pop(node2)
	edges = edges1 + edges2
	# eliminating self loops
	for node in (node1,node2):
		while node in edges:
			edges.remove(node)	

	# making sure the new node is a tuple and push the edges
	if type(node1) == int:
		if type(node2) == int:
			nodes = (node1,) + (node2,)
		else:
			nodes = (node1,) + node2
	elif type(node2) == int:
		nodes = node1 + (node2,)
	else:
		nodes = node1 + node2
		
	graph[nodes] = edges

	# redirecting the other nodes to the super node
	for edge in edges:
		for node in (node1,node2):
			while node in graph[edge]:
				graph[edge].remove(node)
		graph[edge].append(nodes)
	
	return graph
	
def mincut(graph):
	while len(graph) > 2:
		node1 = choice([key for key in graph.keys()])
		node2 = choice(graph[node1])
		readress_node(graph,node1,node2)
	keys = [key for key in graph.keys()]
	return len(graph[keys[0]])
	
def n_cuts(graph,n):
	mcut = []
	for i in range(1,n+1):
		g = graph
		mcut.append(mincut(g))
	return min(mcut)
		

if __name__ == '__main__':
	nodes = []
	edges = []
	with open((sys.argv[1]),'r') as f:
		for row in f:
			lst = row.split('\t')
			lst.remove('\n')
			lst = [int(x) for x in lst]
			nodes.append(lst.pop(0))
			edges.append(lst)
			
	graph = graph_create(nodes,edges)
	min = n_cuts(graph,10000)
	print('minimum crossing edges: {0}'.format(min))
	
	
	

	
				

				
				
				
				