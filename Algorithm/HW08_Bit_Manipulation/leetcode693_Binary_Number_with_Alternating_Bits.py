# 693. Binary Number with Alternating Bits
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/

# Runtime: 36 ms
# Memory Usage: 13.9 MB
# Your runtime beats 78.57 % of python3 submissions.
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n1, n2 = n, n
        
        while (n1&3) == 1:
            n1 >>= 2
        
        while (n2&3) == 2:
            n2 >>= 2
        
        return n1 == 0 or n2 == 0


# Runtime: 40 ms
# Memory Usage: 13.8 MB
# Your runtime beats 44.64 % of python3 submissions.
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n ^= (n>>1)
        return (n & (n+1)) == 0