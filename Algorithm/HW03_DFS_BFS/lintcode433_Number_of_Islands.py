# Leetcode 200 & Lintcode 433 Number of Islands:
# https://www.lintcode.com/problem/number-of-islands/description



# Method 1: DFS
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        self.m, self.n = len(grid), len(grid[0])
        self.visited = set()
        
        
        # DFS
        for i in range(self.m):
            for j in range(self.n):
                if self.is_islands(grid, i, j):
                    self.visited.add((i,j))
                    self.dfs(grid, i, j)
                    islands += 1
        
        return islands
        
    def is_islands(self, grid, x, y):
        return 0 <= x < self.m and 0 <= y < self.n and grid[x][y] == 1 and (x,y) not in self.visited
    
    def dfs(self, grid, x, y):
        
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            x2, y2 = x+dx, y+dy
            
            if self.is_islands(grid, x2, y2) is True:
                self.visited.add((x2,y2))
                self.dfs(grid, x2, y2)






# Method 2: BFS
from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i,j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
        return islands
        
    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        
        while queue:
            idx, idy = queue.popleft()
            for dx, dy in [(1,0), (-1,0), (0, 1), (0, -1)]:
                x2, y2 = idx + dx, idy + dy
                if self.is_valid(grid, x2, y2, visited):
                    queue.append((x2, y2))
                    visited.add((x2, y2))
    
    def is_valid(self, grid, x, y, visited):
        m, n = len(grid), len(grid[0])
        return 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y]