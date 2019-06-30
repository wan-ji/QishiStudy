52. N-Queens II
https://leetcode.com/problems/n-queens-ii/description/


# Runtime: 52 ms
# Memory Usage: 13 MB
# runtime beats 84.45 % of python3 submissions.
# memory usage beats 94.59 % of python3 submissions.

class Solution:
    def totalNQueens(self, n: int) -> int:
        if n <= 0:
            return 0
        
        cols  = [0] * n
        hills = [0] * (2*n - 1)
        dales = [0] * (2*n - 1)
        
        def is_valid(row, idx):
            return not (cols[idx] or hills[row-idx+n-1] or dales[row+idx])
        
        def backtrack(item, row, idx):           
            if row == n:
                return 1
            
            n_solutions = 0
            for i in range(n):
                if not is_valid(row, i):
                    continue
                cols[i] = 1
                hills[row-i+n-1] = 1
                dales[row+i] = 1
                n_solutions += backtrack(item+ [i], row+1, i)
                cols[i] = 0
                hills[row-i+n-1] = 0
                dales[row+i] = 0
                
            return n_solutions
                
        return backtrack([], 0, 0)