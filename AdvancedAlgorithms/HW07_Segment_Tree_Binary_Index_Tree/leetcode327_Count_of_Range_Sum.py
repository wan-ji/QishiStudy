'''
Leetcode 327. Count of Range Sum
https://leetcode.com/problems/count-of-range-sum/

'''

# Solution 1
class BinaryIndexTree:
	def __init__(self, A):
		self.A = A
		self.bit = [0] + A
		self.build_tree()
	
	def build_tree(self):
		for i in range(1, len(self.bit)):
			idx = i + self.lowbit(i)
			if idx < len(self.bit):
				self.bit[idx] += self.bit[i]
	
	def lowbit(self, i):
		return i & (-i)
	
	def update(self, i, val):
		diff = val - self.A[i]
		self.A[i] = val
		idx = i + 1
		while idx < len(self.bit):
			self.bit[idx] += diff
			idx += self.lowbit(idx)
	
	def add(self, i, diff):
		self.A[i] += diff
		idx = i + 1
		while idx < len(self.bit):
			self.bit[idx] += diff
			idx += self.lowbit(idx)
	
	def prefixsum(self, index): # sum(A[:index+1])
		res = 0
		idx = index + 1
		while idx > 0:
			res += self.bit[idx]
			idx -= self.lowbit(idx)
		return res
	
	def rangesum(self, start, end): # sum of A[start:end+1]
		return self.prefixsum(end) - self.prefixsum(start-1) if end >= start else 0


class Solution:
	def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
		A = [0] * (len(nums) + 1)
		for i in range(len(nums)):
			A[i+1] = A[i] + nums[i]
		
		
		sortedA = sorted(A)
		index = {sortedA[0]:0}
		vals = [sortedA[0]]
		
		idx = 0
		for i in range(1, len(sortedA)):
			if sortedA[i] != sortedA[i-1]:
				idx += 1
				index[sortedA[i]] = idx
				vals.append(sortedA[i])
		
		length = len(index)

		
		tree = BinaryIndexTree([0] * length)
		ans = 0
		tree.update(index[0], 1)

		for i in range(1, len(A)):
			start = self.binary_search(vals, A[i] - upper)
			end = self.binary_search(vals, A[i] - lower)
			if end == len(vals) or vals[end] > A[i] - lower:
				end -= 1
			
			
			ans += tree.rangesum(start, end)
			tree.add(index[A[i]], 1)

		return ans
			
			
	
	
	def binary_search(self, vals, value):
		# find the first index i such that vals[i] >= value
		if value <= vals[0]:
			return 0
		if value > vals[-1]:
			return len(vals)
		
		start, end = 0, len(vals) - 1
		while start + 1 < end:
			mid = (start+end)//2
			if vals[mid] < value:
				start = mid + 1
			else:
				end = mid
		
		if vals[start] >= value:
			return start
		return end

		




# Solution 2
class Solution:
	def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
		n = len(nums)
		sums = [0] * (n + 1)
		
		for i in range(n):
			sums[i+1] = sums[i] + nums[i]
		
		return self.count_merge_sort(sums, 0, n+1, lower, upper)
	
	def count_merge_sort(self, sums, start, end, lower, upper):
		if end - start <= 1:
			return 0
		mid = (start + end)//2
		count = self.count_merge_sort(sums, start, mid, lower, upper) + \
				self.count_merge_sort(sums, mid, end, lower, upper)
		
		l, r = mid, mid
		cache = [0] * (end - start)
		t = 0
		s = mid
		
		for i in range(start, mid):
			while l < end and sums[l] - sums[i] < lower:
				l += 1
			while r < end and sums[r] - sums[i] <= upper:
				r += 1
			while s < end and sums[s] < sums[i]:
				cache[t] = sums[s]
				s += 1
				t += 1
			cache[t] = sums[i]
			t += 1
			
			count += r - l
		
		sums[start:(start+t)] = cache[:t]
		
		return count

