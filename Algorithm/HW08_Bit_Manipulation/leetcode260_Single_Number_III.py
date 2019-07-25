# 260. Single Number III
# https://leetcode.com/problems/single-number-iii/description/

# Runtime: 68 ms
# Memory Usage: 15.8 MB
# Your runtime beats 80.56 % of python3 submissions.
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0
        for i in nums:
            mask ^= i
        
        shift = 1
        while mask & 1 == 0:
            mask >>= 1
            shift <<= 1
        
        num1, num2 = 0, 0
        for i in nums:
            if (shift & i) == 0:
                num1 ^= i
            else:
                num2 ^= i
        
        return [num1, num2]