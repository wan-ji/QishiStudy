# 79. Word Search
# https://leetcode.com/problems/word-search/description/


# Runtime: 296 ms
# Memory Usage: 13.7 MB
# runtime beats 43.40 % of python3 submissions
# memory usage beats 97.25 % of python3 submissions
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        
        visited = [[False for _ in range(len(board[0]))] for __ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self.dfs(visited, board, word, 1, i, j):
                        return True
                    visited[i][j] = False
        
        return False

    
    def dfs(self, visited, board, word, idx, x, y):
        if idx == len(word):
            return True
        
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            x2, y2 = x + dx, y + dy
            if self.is_valid(visited, board, word[idx], x2, y2):
                visited[x2][y2] = True
                if self.dfs(visited, board, word, idx+1, x2, y2):
                    return True
                visited[x2][y2] = False
        return False
    
            
    def is_valid(self, visited, board, ch, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == ch and not visited[x][y]
        
