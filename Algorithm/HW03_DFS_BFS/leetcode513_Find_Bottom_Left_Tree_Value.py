# Leetcode 513 Find Bottom Left Tree Value:
# https://leetcode.com/problems/find-bottom-left-tree-value/



# Method 1: BFS
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        level = [root]
        last_level = []
        
        while level:
            new_level = []
            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            
            if not new_level:
                last_level = level
                
            level = new_level
        
        return last_level[0].val



# Method 1: DFS
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # write your code here
        self.max_level = 0
        self.val = None
        self.dfs(root, 1)
        
        return self.val
    
    def dfs(self, root, level):
        if not root:
            return
        if level > self.max_level:
            self.val = root.val
            self.max_level = level
        
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)