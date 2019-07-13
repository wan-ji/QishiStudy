# 486. Predict the Winner
# https://leetcode.com/problems/predict-the-winner/description/




# Runtime: 28 ms
# Memory Usage: 13.1 MB
# Your runtime beats 99.54 % of python3 submissions.
# Your memory usage beats 75.77 % of python3 submissions.
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [i for i in nums]
        
        for l in range(1, len(nums)):
            for i in range(len(nums) - l):
                dp[i] = max(nums[i] - dp[i+1], nums[i+l] - dp[i])
        
        return dp[0] >= 0



# Runtime: 36 ms
# Memory Usage: 13.1 MB
# Your runtime beats 87.75 % of python3 submissions.
# Your memory usage beats 84.02 % of python3 submissions.
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[0] * len(nums) for _ in range(len(nums))]
        
        for i in range(len(nums)):
            dp[i][i] = nums[i]
              
        for l in range(1, len(nums)):
            for i in range(len(nums)-l):
                dp[i][i+l] = max(nums[i] - dp[i+1][i+l], nums[i+l] - dp[i][i+l-1])
        
        return dp[0][-1] >= 0


