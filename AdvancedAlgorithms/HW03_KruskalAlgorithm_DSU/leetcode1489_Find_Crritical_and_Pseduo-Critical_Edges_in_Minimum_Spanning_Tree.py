'''
Leetcode 1489 Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

'''

class UnionFind:
    
    def __init__(self, n):
        self.father = list(range(n))
        self.rootCount = n
    
    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]
        
        for i in path:
            self.father[i] = node
        
        return node
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 == root2:
            return
        else:
            self.father[root1] = root2
        
        self.rootCount -= 1
        
        
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        sortedEdges = sorted(enumerate(edges), key=lambda x:x[1][2])
        
        def kruskal(preAdd, ban):
            uf = UnionFind(n)
            weights = 0
            
            if preAdd >= 0:
                _, (u, v, w) = sortedEdges[preAdd]
                uf.union(u, v)
                weights += w
                if uf.rootCount == 1:
                    return weights
            
            for i in range(len(sortedEdges)):
                if i == ban or i == preAdd:
                    continue
                _, (u, v, w) = sortedEdges[i]
                if uf.find(u) != uf.find(v):
                    uf.union(u, v)
                    weights += w
                    if uf.rootCount == 1:
                        return weights
            
            return 1e9
        
        MSTw = kruskal(-1, -1)
        ans = [[], []]
        
        for i in range(len(sortedEdges)):
            weight = kruskal(-1, i)
            if weight > MSTw:
                ans[0].append(sortedEdges[i][0])
            else:
                weight = kruskal(i, -1)
                if weight == MSTw:
                    ans[1].append(sortedEdges[i][0])
        
        return ans






