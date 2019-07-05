# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# Runtime: 40 ms
# Memory Usage: 13.7 MB
# Your runtime beats 84.90 % of python3 submissions.
# Your memory usage beats 53.21 % of python3 submissions.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return []
        return self.helper(nums, k)
        
    def helper(self, nums, k):
        if len(nums) == 1:
            return nums[0]
        
        left, right = [], []
        mid = nums[len(nums)//2]
        nmid = 0
        
        for i in nums:
            if i == mid:
                nmid += 1
            elif i < mid:
                left.append(i)
            else:
                right.append(i)
        
        if len(right) < k and len(right) + nmid >= k:
            return mid

        if len(right) < k:
            return self.helper(left, k - len(right) - nmid)
        else:
            return self.helper(right, k)