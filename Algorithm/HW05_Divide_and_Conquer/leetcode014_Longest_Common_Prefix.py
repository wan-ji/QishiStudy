# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/


# Divide and Conquer Solution
# Runtime: 40 ms
# Memory Usage: 13.1 MB
# runtime beats 56.48 % of python3 submissions.
# memory usage beats 90.17 % of python3 submissions.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        return self.helper(strs, 0, len(strs)-1)
    
    def helper(self, strs, left, right):
        if left == right:
            return strs[left]
        
        mid = (left + right) // 2
        leftprefix = self.helper(strs, left, mid)
        if len(leftprefix) == 0:
            return ""
        rightprefix = self.helper(strs, mid + 1, right)
        if len(rightprefix) == 0:
            return ""

        idx = 0
        while idx < len(leftprefix) and idx < len(rightprefix):
            if  leftprefix[idx] != rightprefix[idx]:
                break
            idx += 1
        
        return leftprefix[:idx]






# Reference:
# https://leetcode.com/problems/longest-common-prefix/discuss/172553/beat-100-python-submission-short-and-clean
# Runtime: 36 ms
# Memory Usage: 13.4 MB
# runtime beats 85.10 % of python3 submissions
# memory usage beats 5.57 % of python3 submissions
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        s1 = min(strs)
        s2 = max(strs)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1



# Reference:
# https://leetcode.com/problems/longest-common-prefix/discuss/7235/A-pythonic-solution-52-ms
# Runtime: 36 ms
# Memory Usage: 13.2 MB
# runtime beats 85.10 % of python3 submissions.
# memory usage beats 49.94 % of python3 submissions.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for z in zip(*strs):
            bag = set(z)
            if len(bag) == 1:
                prefix += bag.pop()
            else:
                break
        return prefix