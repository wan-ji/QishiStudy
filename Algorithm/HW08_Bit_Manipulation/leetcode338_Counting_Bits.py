# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/description/

# Method 1
# Runtime: 68 ms
# Memory Usage: 15.9 MB
# Your runtime beats 79.72 % of python submissions.
# Your memory usage beats 13.14 % of python submissions.
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        nbits = [0] * (num + 1)
        pow2int = 1
        
        for i in range(1, num+1):
            if i < pow2int * 2:
                nbits[i] = nbits[i-pow2int] + 1
            else:
                pow2int <<= 1
                nbits[i] = 1
        
        return nbits


# Method 2
# Reference:
# https://leetcode.com/problems/counting-bits/discuss/79539/Three-Line-Java-Solution
# Runtime: 64 ms
# Memory Usage: 15.9 MB
# Your runtime beats 90.51 % of python submissions.
# Your memory usage beats 7.30 % of python submissions.
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        nbits = [0] * (num + 1)
        
        for i in range(1, num+1):
            nbits[i] = nbits[(i>>1)] + (i&1)
        
        return nbits




# Method 3
# Reference:
# https://leetcode.com/problems/counting-bits/discuss/79527/Four-lines-C++-time-O(n)-space-O(n)
# Runtime: 64 ms
# Memory Usage: 15.9 MB
# Your runtime beats 90.51 % of python submissions.
# Your memory usage beats 13.14 % of python submissions.
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        nbits = [0] * (num + 1)
        
        for i in range(1, num+1):
            nbits[i] = nbits[(i>>1)] + (i&1)
        
        return nbits