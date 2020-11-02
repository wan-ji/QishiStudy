'''
Leetcode 338. Counting Bits
https://leetcode.com/problems/counting-bits/

'''

class Solution:
	def countBits(self, num: int) -> List[int]:
		nbits = [0] * (num + 1)
		
		for i in range(1, num + 1):
			nbits[i] = nbits[i&(i-1)] + 1
		
		return nbits

class Solution:
	def countBits(self, num: int) -> List[int]:
		nbits = [0] * (num + 1)
		
		for i in range(1, num + 1):
			nbits[i] = nbits[i>>1] + (i&1)
		
		
		return nbits