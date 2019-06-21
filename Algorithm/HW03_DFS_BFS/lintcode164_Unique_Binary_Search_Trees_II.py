# Lintcode 164 Unique Binary Search Trees II
# https://www.lintcode.com/problem/unique-binary-search-trees-ii/description

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        # write your code here
        return self.dfs(1,n)
    
    def dfs(self, start, end):
        if start > end:
            return [None]
        
        roots = []
        
        for val in range(start, end+1):
            leftTree = self.dfs(start, val-1)
            rightTree = self.dfs(val +1, end)
            
            for i in leftTree:
                for j in rightTree:
                    root = TreeNode(val)
                    root.left = i
                    root.right = j
                    roots.append(root)
                    
            
        return roots
                    
        
        
        
        

        
        
        
        
        
        
        