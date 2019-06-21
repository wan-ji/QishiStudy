# Lintcode 376. Binary Tree Path Sum
# https://www.lintcode.com/problem/binary-tree-path-sum/description

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        if not root or not target:
            return []
        
        
        path = []
        result = []
        
        self.dfs(root, target, path, result, 0)

        return result
    
    def dfs(self, node, target, path, result, summation):
        if not node:
            return
        path.append(node.val)
        summation += node.val
        
        if not node.left and not node.right and summation==target:
            result.append(path[:])
        
        self.dfs(node.left, target, path, result, summation)
        self.dfs(node.right, target, path, result, summation)
        
        path.pop()

        
        
        
        
        
        
        
        
        