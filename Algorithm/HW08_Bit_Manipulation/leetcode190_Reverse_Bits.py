# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/description/


# Method 1
# Runtime: 16 ms
# Memory Usage: 11.9 MB
# Your runtime beats 86.36 % of python submissions.
# Your memory usage beats 11.00 % of python submissions.
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans <<= 1
            if (n & 1) == 1:
                ans += 1
            n >>= 1
        return ans


# Method 2
# Runtime: 24 ms
# Memory Usage: 11.8 MB
# Your runtime beats 41.07 % of python submissions.
# Your memory usage beats 28.71 % of python submissions.
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        for i,j in zip(range(16), range(31, 15, -1)):
            n += ((n & (1 << i)) << (j-i)) + ((n & (1 << j)) >> (j-i)) - (n & (1 << i)) - (n & (1 << j))
        return n
