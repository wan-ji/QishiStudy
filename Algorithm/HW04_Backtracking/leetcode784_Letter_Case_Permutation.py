# 784. Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation/description/

# Solution 1
# Runtime: 88 ms
# Memory Usage: 14.2 MB
# runtime beats 40.92 % of python3 submissions.
# memory usage beats 21.33 % of python3 submissions.

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return []
        Slist = list(S)
        ans = []
        self.backtrack(Slist, ans, [], 0)
        
        return list(map("".join, ans))
        
    
    def backtrack(self, Slist, ans, temp, idx):
        if idx == len(Slist):
            ans.append(temp)
            return
        
        idx2 = idx
        while idx2 < len(Slist):
            if Slist[idx2].isalpha():
                self.backtrack(Slist, ans, temp + Slist[idx:idx2]+ [Slist[idx2].lower()], idx2+1)
                self.backtrack(Slist, ans, temp + Slist[idx:idx2]+ [Slist[idx2].upper()], idx2+1)
                return
            idx2 += 1
        
        if idx2 == len(Slist):
            
            ans.append(temp + Slist[idx:])
        
        return


# Solution 2
# Reference:
# https://leetcode.com/problems/letter-case-permutation/solution/
# Runtime: 72 ms
# Memory Usage: 14.7 MB
# runtime beats 86.47 % of python3 submissions.
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = [[]]
        
        for char in S:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n+i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)
                    
        return list(map("".join, ans))

