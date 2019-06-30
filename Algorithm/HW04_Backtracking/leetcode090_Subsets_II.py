# 90. Subsets II
# https://leetcode.com/problems/subsets-ii/description/



# Runtime: 44 ms
# Memory Usage: 13.6 MB
# runtime beats 90.38 % of python3 submissions.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        ans = []
        def proceed(comb, idx):
            ans.append(comb)
            
            if idx == len(nums):
                return

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                proceed(comb + [nums[i]], i + 1)
                
        proceed([],0)
        
        return ans



# Runtime: 44 ms
# Memory Usage: 13.4 MB
# runtime beats 90.38 % of python3 submissions.
# memory usage beats 18.46 % of python3 submissions.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        
        ans = [[]]
        lastidx = [-1]
        
        
        for i in range(len(nums)):
            size = len(ans)
            for s in range(size):
                if i > 0 and nums[i] == nums[i-1] and lastidx[s] != i-1:
                    continue
                ans.append(ans[s] + [nums[i]])
                lastidx.append(i)

        return ans