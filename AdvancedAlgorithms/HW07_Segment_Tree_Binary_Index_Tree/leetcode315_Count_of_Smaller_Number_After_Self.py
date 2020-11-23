'''
Leetcode 315. Count of Smaller Numbers After Self
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

'''

# Solution 1
class Solution:
	def countSmaller(self, nums: List[int]) -> List[int]:
		n = len(nums)
		rank = {val: i + 1 for i, val in enumerate(sorted(list(set(nums))))}
		
		bitTree = [0] * (n+1)
		
		def update(index):
			while index <= n:
				bitTree[index] += 1
				index += index &(-index)
		
		def getSum(index):
			res = 0
			while index > 0:
				res += bitTree[index]
				index -= index & (-index)
			return res
		
		ans = [0] * n
		for i in range(n-1, -1, -1):
			ans[i] = getSum(rank[nums[i]] - 1)
			update(rank[nums[i]])
		
		return ans




# Solution 2
class Solution:
	def countSmaller(self, nums: List[int]) -> List[int]:
		ans = [0] * len(nums)
		A = list(range(len(nums)))
		
		def count(start, end):
			if end - start <= 1:
				return
			
			mid = (start + end)//2
			count(start, mid)
			count(mid, end)
			
			i, j = start, mid
			sorted_A = [0] * (end - start)
			idx = 0
			
			for i in range(start, mid):
				while j < end and nums[A[i]] > nums[A[j]]:
					sorted_A[idx] = A[j]
					j += 1
					idx += 1
				
				sorted_A[idx] = A[i]
				ans[A[i]] += j - mid
				idx += 1
			
			A[start:start+idx] = sorted_A[:idx]
			
			return
		
		count(0, len(nums))
		
		return ans

