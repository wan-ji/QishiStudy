# 201. Bitwise AND of Numbers Range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/

# Runtime: 44 ms
# Memory Usage: 11.7 MB
# Your runtime beats 78.69 % of python submissions.
# Your memory usage beats 51.90 % of python submissions.
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        idx = n.bit_length() - 1
        ans = 0
        while idx >= 0 and (m & (1 << idx)) == (n & (1 << idx)):
            ans += (m & (1 << idx))
            idx += -1

        return ans




# Method 2
# Reference:
# https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56729/Bit-operation-solution(JAVA)
# Runtime: 44 ms
# Memory Usage: 11.8 MB
# Your runtime beats 78.69 % of python submissions.
# Your memory usage beats 26.58 % of python submissions.
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        factor = 1
        while m != n:
            m >>= 1
            n >>= 1
            factor <<= 1
        
        return factor * n
