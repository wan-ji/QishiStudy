'''
Leetcode 214. Shortest Palindrome
https://leetcode.com/problems/shortest-palindrome/

'''

class Solution:
	def shortestPalindrome(self, s: str) -> str:
		if len(s) <= 1:
			return s
		
		f = [0] * len(s)
		idx = 0
		for i in range(1, len(s)):
			while idx and s[idx] != s[i]:
				idx = f[idx-1]
			idx += s[i] == s[idx]
			f[i] = idx
		
		idx = 0
		
		for i in range(len(s)):
			while idx and s[idx] != s[~i]:
				idx = f[idx-1]
			idx += s[idx] == s[~i]

		return s[:idx-1:-1] + s
