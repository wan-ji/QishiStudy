# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/description/

# Runtime: 32 ms
# Memory Usage: 13.3 MB
# runtime beats 90.75 % of python3 submissions.
# memory usage beats 33.12 % of python3 submissions.
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        
        ans = 1
        while n >= 1:
            if n%2 == 1:
                ans = ans * x
                n = n - 1
            else:
                x = x * x
                n = n//2

        return ans
