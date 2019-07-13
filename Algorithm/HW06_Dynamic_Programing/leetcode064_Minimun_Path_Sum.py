# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/description/

# Runtime: 48 ms
# Memory Usage: 13.3 MB
# Your runtime beats 93.24 % of python3 submissions.
# Your memory usage beats 98.51 % of python3 submissions.
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        pathsum = [i for i in grid[0]]
        
        for i in range(1, len(grid[0])):
            pathsum[i] += pathsum[i-1]
        
        for i in range(1, len(grid)):
            pathsum[0] += grid[i][0]
            for j in range(1, len(grid[0])):
                pathsum[j] = grid[i][j] + min(pathsum[j-1], pathsum[j])
        
        return pathsum[-1]


