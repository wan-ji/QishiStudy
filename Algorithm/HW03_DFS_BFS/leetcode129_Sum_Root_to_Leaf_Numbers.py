# Leetcode 129 Sum Root to Leaf Numbers:
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Method 1

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.sums = 0
        p = []
        
        self.dfs(root, p)
        
        return self.sums
    
    def dfs(self, root, p):
        p.append(root.val)
        
        if not root.left and not root.right:
            self.sums += int(''.join(map(str, p)))
            p.pop()
            return
        
        if root.left:
            self.dfs(root.left, p)
        if root.right:
            self.dfs(root.right, p)
        
        p.pop()

# Method 2:
# Reference: 
# https://www.jiuzhang.com/solution/sum-root-to-leaf-numbers/#tag-highlight-lang-python
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)
    
    def dfs(self, root, pre):
        if not root:
            return 0
        sums = root.val + pre*10
        
        if not root.left and not root.right:
            return sums
        
        return self.dfs(root.left, sums) + self.dfs(root.right, sums)