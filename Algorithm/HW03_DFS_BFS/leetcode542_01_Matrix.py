# Leetcode 542 01 Matrix:
# https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return None
        
        self.m, self.n = len(matrix), len(matrix[0])
        ans = [[0 for j in range(self.n)] for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if matrix[i][j]: # if matrix[i][j] == 0, distance is 0
                    ans[i][j] = self.find_distance(matrix, i, j)
        
        return ans
    
    def find_distance(self, matrix, i, j):
        level = [(i,j)]
        visited = set()
        visited.add((i,j))
        
        step = 1
        
        while level:
            new_level = []
            for (x, y) in level:
                for (dx, dy) in [(-1,0), (1,0), (0,-1), (0,1)]:
                    x2, y2 = x + dx, y + dy
                    if 0 <= x2 < self.m and 0 <= y2 < self.n and (x2, y2) not in visited:
                        if matrix[x2][y2] == 0:
                            return step
                        else:
                            new_level.append((x2,y2))
                            visited.add((x2,y2))
            step += 1
            level = new_level
            
        return -1
                        
                
                
        
        
        