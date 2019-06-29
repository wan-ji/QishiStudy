# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/description/

# Runtime: 48 ms
# Memory Usage: 13.2 MB
# runtime beats 92.78 % of python3 submissions.
# memory usage beats 66.34 % of python3 submissions.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        candidates.sort()
        ans = []
        
        def backtrack(comb, idx, target):
            if target == 0:
                ans.append(comb)
                return
            if idx >= len(candidates) or candidates[idx] > target:
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if target >= candidates[i]:
                    backtrack(comb + [candidates[i]], i+1, target - candidates[i])
        
        backtrack([], 0, target)
        
        return ans