# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/



# Runtime: 40 ms
# Memory Usage: 13.2 MB
# runtime beats 84.84 % of python3 submissions.
# memory usage beats 83.06 % of python3 submissions.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []
        
        ans = []
        self.back_track(ans, '', n, 0, 0)
        return ans
    
    def back_track(self, ans, comb, n, n_l, n_r):
        if len(comb) == 2*n:
            ans.append(comb)
            return
        if n_l < n:
            self.back_track(ans, comb + '(', n, n_l + 1, n_r)
        if n_l > n_r:
            self.back_track(ans, comb + ')', n, n_l, n_r + 1)
        return