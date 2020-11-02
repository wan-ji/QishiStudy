'''
Leetcode 1392. Longest Happy Prefix
https://leetcode.com/problems/longest-happy-prefix/

'''

class Solution:
	def longestPrefix(self, s: str) -> str:
		f = [0] * len(s)
		
		idx = 0
		for i in range(1, len(s)):
			while idx and s[idx] != s[i]:
				idx = f[idx-1]
			idx += s[idx] == s[i]
			f[i] = idx
		
		return s[:idx]