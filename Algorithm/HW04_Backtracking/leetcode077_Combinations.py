# 77. Combinations
# https://leetcode.com/problems/combinations/description/




# Runtime: 568 ms
# Memory Usage: 15 MB
# runtime beats 61.88 % of python3 submissions.
# memory usage beats 61.65 % of python3 submissions.
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n or not k or n < k:
            return []
        
        ans = []
        
        def proceed(comb, idx):
            if len(comb) == k:
                ans.append(comb)
                
            if idx > n:
                return
                    
            for i in range(idx, n+1):
                proceed(comb + [i], i + 1)
                
        proceed([], 1)
        
        return ans


