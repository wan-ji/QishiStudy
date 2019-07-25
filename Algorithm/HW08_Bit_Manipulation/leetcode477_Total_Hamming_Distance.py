# 477. Total Hamming Distance
# https://leetcode.com/problems/total-hamming-distance/description/


# Runtime: 736 ms
# Memory Usage: 14.8 MB
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 0
        ndigits = max(nums).bit_length()
        for i in range(ndigits):
            n1 = 0
            for i in range(len(nums)):
                n1 += nums[i] & 1
                nums[i] >>= 1
            ans += (len(nums) - n1) * n1
        return ans