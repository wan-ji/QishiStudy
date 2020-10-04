
from collections import defaultdict



class HashHeap:
	def __init__(self, desc=False):
		self.hash = dict()
		self.heap = []
		self.desc = desc
	
	@property
	def size(self):
		return len(self.heap)
	
	def push(self, item):
		self.heap.append(item)
		self.hash[item] = self.size - 1
		self._sift_up(self.size - 1)
	
	def pop(self):
		item = self.heap[0]
		self.remove(item)
		return item
	
	def top(self):
		return self.heap[0]
	
	def remove(self, item):
		if item not in self.hash:
			return 
		
		index = self.hash[item]
		self._swap(index, self.size - 1)
		
		del self.hash[item]
		self.heap.pop()
		
		if index < self.size:
			self._sift_up(index)
			self._sift_down(index)
		
	def _smaller(self, left, right):
		return right < left if self.desc else left < right
	
	def _sift_up(self, index):
		while index != 0:
			parent = (index-1) // 2
			if self._smaller(self.heap[parent], self.heap[index]):
				break
			self._swap(parent, index)
			index = parent
			
	def _sift_down(self, index):
		if index is None:
			return
		while index * 2 + 1 < self.size:
			smallest = index
			left = index * 2 + 1
			right = index * 2 + 2
			
			if self._smaller(self.heap[left], self.heap[smallest]):
				smallest = left
			
			if right < self.size and  self._smaller(self.heap[right], self.heap[smallest]):
				smallest = right
			
			if smallest == index:
				break
			
			self._swap(index, smallest)
			index = smallest
	
	def _swap(self, i, j):
		elem1, elem2 = self.heap[i], self.heap[j]
		self.heap[i], self.heap[j] = elem2, elem1
		self.hash[elem1], self.hash[elem2] = j, i








def AStar(edges, start, target, heuristic):
	graph = defaultdict(list)

	for u, v, w in edges:
		graph[u].append((v, w))
		graph[v].append((u, w))

	openSet = HashHeap()
	openSet.push((heuristic[start], 0, start))
	gScores = {start:0}



	while openSet:
		f, g, node = openSet.pop()

		if node == target:
			# print(openSet.heap)
			return g

		for v, w in graph[node]:
			g2 = g + w

			if v not in gScores or g2 < gScores[v]:
				
				if v in gScores:
					# print('to remove', (gScores[v] + heuristic[v], gScores[v], v))
					openSet.remove((gScores[v] + heuristic[v], gScores[v], v))

				gScores[v] = g2
				# print('to add', (g2 + heuristic[v], g2, v))
				openSet.push((g2 + heuristic[v], g2, v))

	print(openSet.heap)
	return -1



	

def test():
	edges = [('A', 'B', 6), ('A', 'F', 3), ('B', 'C', 3), ('B', 'D', 2),\
			('C', 'D', 1), ('C', 'E', 5), ('D', 'E', 8), ('E', 'I', 5),\
			('E', 'J', 5), ('F', 'G', 1), ('F', 'H', 7), ('G', 'I', 3),\
			('H', 'I', 2), ('I', 'J', 3)]
	heuristic = {'A':10, 'B':6, 'C':5, 'D':7, 'E':3, 'F':6, 'G':5, 'H':3, 'I':1, 'J':0}

	print(AStar(edges, 'A', 'J', heuristic))
	# print((1,2) < (2,3))




test()


	





  