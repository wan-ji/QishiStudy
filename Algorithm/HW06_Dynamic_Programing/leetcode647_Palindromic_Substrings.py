# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/description/



# Runtime: 36 ms
# Memory Usage: 13.1 MB
# Your runtime beats 100.00 % of python3 submissions.
# Your memory usage beats 86.03 % of python3 submissions.
class Solution:
    def countSubstrings(self, s: str) -> int:
        # store the left index of longest palindromic substrings ending in current index
        leftidx = [0]
        len_same_char = 1
        count = 1
        
        for i in range(1, len(s)):
            # check palindromic substrings with same character first
            if s[i - 1] == s[i]:
                len_same_char += 1
            else:
                len_same_char = 1
            
            count += len_same_char
            
            # deal with palindromic substrings with different characters
            new_leftidx = [i-len_same_char+1]
            for idx in leftidx:
                if idx - 1 >= 0 and s[idx-1] == s[i]:
                    count += 1
                    new_leftidx.append(idx - 1)

            
            leftidx = new_leftidx

        
        return count




# Runtime: 132 ms
# Memory Usage: 13.1 MB
# Your runtime beats 72.23 % of python3 submissions.
# Your memory usage beats 75.40 % of python3 submissions.
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(2*len(s)):
            left = i//2
            right = left + i%2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left  += -1
                right += 1
                ans += 1

        return ans


