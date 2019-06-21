# Leetcode 934 Shortest Bridge:
# https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        self.m, self.n = len(A), len(A[0])
        island0 = set()
        visited0 = set()
        queue_island = collections.deque([])
        
        
        # Find the first islands
        for i in range(self.m):
            for j in range(self.n):
                if not island0 and A[i][j] and (i,j) not in island0:
                    queue_island = self.bfs(A, i, j, island0)
    
        # Find the shortest step
        step = 0
        visited = set()
        level = list(island0)
        while level:
            new_level = []
            for (x,y) in level:
                for (dx, dy) in [(-1,0), (1,0), (0,-1), (0,1)]:
                    x2, y2 = x + dx, y + dy
                    if 0 <= x2 < self.m and 0 <= y2 < self.n and (x2, y2) not in island0 and (x2, y2) not in visited:
                        if A[x2][y2]:
                            return step
                        else:
                            visited.add((x2,y2))
                            new_level.append((x2,y2))
                            
            step += 1
            level = new_level

        return -1
    
    def bfs(self, A, i, j, island0):
        queue = collections.deque([(i,j)])
        island0.add((i, j))
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                x2, y2 = x + dx, y + dy
                if self.is_valid(A, x2, y2, island0):
                    island0.add((x2, y2))
                    self.bfs(A, x2, y2, island0)
    
    def is_valid(self, A, x, y, island):
        return 0 <= x < self.m and 0 <= y < self.n and A[x][y] and (x,y) not in island


        