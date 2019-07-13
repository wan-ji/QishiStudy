# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/

# Runtime: 44 ms
# Memory Usage: 13.7 MB
# Your runtime beats 69.36 % of python3 submissions.
# Your memory usage beats 40.51 % of python3 submissions.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)




# Divide and Conquer Approach
# Runtime: 132 ms
# Memory Usage: 13.5 MB
# Your memory usage beats 90.96 % of python3 submissions.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, nums, left, right):
        if left == right:
            return nums[left]
        
        p = (left + right) // 2
        
        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p+1, right)
        cross_sum = self.cross_sum(nums, left, right, p)
        
        return max(left_sum, right_sum, cross_sum)
    
    def cross_sum(self, nums, left, right, p):
        l, r = p-1, p+1
        sums = nums[p]
        leftsum, rightsum = 0, 0
        leftmax, rightmax = 0, 0
        
        while l >= left:
            leftsum += nums[l]
            leftmax = max(leftmax, leftsum)
            l += -1
        while r <= right:
            rightsum += nums[r]
            rightmax = max(rightmax, rightsum)
            r += 1
        
        if leftmax > 0:
            sums += leftmax
        if rightmax > 0:
            sums += rightmax
        return sums
            
        