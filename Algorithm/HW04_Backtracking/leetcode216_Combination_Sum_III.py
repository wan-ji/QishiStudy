# 216. Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/description/


# Runtime: 36 ms
# Memory Usage: 13.1 MB
# runtime beats 83.48 % of python3 submissions
# memory usage beats 77.60 % of python3 submission
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k is None or n is None or n < k:
            return []
        
        ans = []
        
        def proceed(comb, lens, start_n, target):
            if lens == 0:
                if target == 0:
                    ans.append(comb)
                return
            
            for i in range(start_n, 10):
                if i <= target:
                    proceed(comb + [i], lens - 1, i + 1, target - i)
        
        proceed([], k, 1, n)
        
        return ans