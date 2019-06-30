# 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/description/


# Runtime: 104 ms
# Memory Usage: 13.7 MB
# runtime beats 63.37 % of python3 submissions.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        ans = []
        
        def is_Palindrome(s):
            return s == s[::-1]
        
        def backtrack(comb, idx):
            if idx == len(s):
                ans.append(comb)
                return
            for i in range(idx+1, len(s)+1):
                if is_Palindrome(s[idx:i]):
                    backtrack(comb + [s[idx:i]], i)

        backtrack([],0)
            
        return ans