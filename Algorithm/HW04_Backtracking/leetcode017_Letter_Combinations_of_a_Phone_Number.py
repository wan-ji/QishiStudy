# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# Solution 1
# Runtime: 32 ms
# Memory Usage: 13.2 MB
# runtime beats 93.31 % of python3 submissions.
# memory usage beats 44.87 % of python3 submissions.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        maps = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
                '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
                '8':['t','u','v'], '9':['w','x','y','z']}
        ans = ['']
        
        for s in digits:
            ans = [i + j for i in ans for j in maps[s]]
        
        return ans


# Solution 1
# Runtime: 32 ms
# Memory Usage: 13.2 MB
# runtime beats 93.31 % of python3 submissions.
# memory usage beats 44.29 % of python3 submissions.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        maps = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
                '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
                '8':['t','u','v'], '9':['w','x','y','z']}
        
        ans = []
        
        def backtrack(comb, idx):
            if idx == len(digits):
                ans.append(comb)
                return
            for letter in maps[digits[idx]]:
                backtrack(comb + letter, idx+1)
        
        if len(digits) > 0:
            backtrack("", 0)

            
        return ans