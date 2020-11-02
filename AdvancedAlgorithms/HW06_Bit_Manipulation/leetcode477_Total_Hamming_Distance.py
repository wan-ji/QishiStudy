'''
Leetcode 477. Total Hamming Distance
https://leetcode.com/problems/total-hamming-distance/

'''

class Solution:
	def totalHammingDistance(self, nums: List[int]) -> int:
		ans = 0
		n = len(nums)
		
		for d in range(32):
			n1 = 0
			for i in range(len(nums)):
				n1 += nums[i] & 1
				nums[i] >>= 1
			ans += (n - n1) * n1
		
		return ans