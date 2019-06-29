# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/description/



# Reference
# https://leetcode.com/problems/permutations-ii/discuss/18602/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others-:-)
# Runtime: 64 ms
# Memory Usage: 13.4 MB
# runtime beats 97.98 % of python3 submissions.
# memory usage beats 41.91 % of python3 submissions.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        ans = [[]]
        for n in nums:
            new_ans = []
            for a in ans:
                for i in range(len(a)+1):
                    new_ans.append(a[:i] + [n] + a[i:])
                    if i < len(a) and a[i] == n:
                        break
            ans = new_ans
        
        return ans


# Reference
# https://leetcode.com/problems/permutations-ii/discuss/18602/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others-:-)
# Runtime: 84 ms
# Memory Usage: 13.7 MB
# runtime beats 45.27 % of python3 submissions.
# memory usage beats 10.45 % of python3 submissions.
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        ans = []
        
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                ans.append(comb[:])
            for x in counter:
                if counter[x] > 0:
                    counter[x] += -1
                    backtrack(comb + [x], counter)
                    counter[x] += 1
        
        backtrack([], collections.Counter(nums))
                    
        return ans