# 783. Minimum Risk Path
# https://www.lintcode.com/problem/minimum-risk-path/description

# Total runtime: 68ms
class Solution:
    """
    @param n: maximum index of position.
    @param m: the number of undirected edges.
    @param x: 
    @param y: 
    @param w: 
    @return: return the minimum risk value.
    """
    def getMinRiskValue(self, n, m, x, y, w):
        edges = sorted(zip(w,x,y))
            
        father = [i for i in range(n+1)]
        risk = 0
        
        for r, u, v in edges:
            root1 = self.find(father, u)
            root2 = self.find(father, v)
            
            if root1 != root2:
                father[root1] = root2
                risk = max(risk, r)
            
            if self.find(father, 0) == self.find(father,n):
                return risk
        
        return -1
    
    def find(self, father, node):
        if father[node] == node:
            return node
        root = self.find(father, father[node])
        father[node] = root
        return root