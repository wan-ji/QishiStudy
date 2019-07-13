# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/

# Runtime: 32 ms
# Memory Usage: 13.1 MB
# Your runtime beats 87.00 % of python3 submissions.
# Your memory usage beats 62.43 % of python3 submissions.
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp1, dp2 = 1, 2
        for i in range(n-2):
            dp1, dp2 = dp2, dp1 + dp2
        
        return dp2


