718. Maximum Length of Repeated Subarray
https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/


# Runtime: 2188 ms
# Memory Usage: 13.3 MB
# Your runtime beats 93.51 % of python3 submissions.
# Your memory usage beats 89.32 % of python3 submissions.
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [0] * n
        maxlen = 0
        
        for i in range(m):
            for j in range(n-1, 0, -1):
                dp[j] = dp[j-1] + 1 if A[i] == B[j] else 0
            dp[0] = int(A[i] == B[0])
            maxlen = max(maxlen, max(dp))
        
        return maxlen