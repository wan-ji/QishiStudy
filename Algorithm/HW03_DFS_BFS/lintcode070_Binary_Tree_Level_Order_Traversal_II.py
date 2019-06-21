# Leetcode 107 & Lintcode 70 Binary Tree Level Order Traversal II: 
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# https://www.lintcode.com/problem/binary-tree-level-order-traversal-ii/description


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        if not root:
            return []
            
        ans = []
        queue = collections.deque([root])
        
        while queue:
            length = len(queue)
            level = []
            for _ in range(length):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            ans = [level] + ans
        
        return ans