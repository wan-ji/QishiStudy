# 46. Permutations
# https://leetcode.com/problems/permutations/description/

# Runtime: 44 ms
# Memory Usage: 13.4 MB
# runtime beats 97.83 % of python3 submissions.
# memory usage beats 26.23 % of python3 submissions.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        ans = []
        
        def backtrack(comb, numslist):
            if len(numslist) == 0:
                ans.append(comb)
                return
            
            for i in range(len(numslist)):
                backtrack(comb + [numslist[i]], numslist[:i] + numslist[i+1:])
        
        backtrack([], nums)
        
        return ans



# Solution 2
# Reference:
# https://leetcode.com/problems/permutations/solution/
# Runtime: 52 ms
# Memory Usage: 13.6 MB
# runtime beats 72.74 % of python3 submissions.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        ans = []
        
        def backtrack(first):
            if first == len(nums):
                ans.append(nums[:])
                return
            
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        
        return ans