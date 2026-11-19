# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxParentVal):
            if not node:
                return 0
            
            maxParentVal = max(node.val, maxParentVal)

            if node.val >= maxParentVal:
                return dfs(node.left, maxParentVal) + dfs(node.right, maxParentVal)+ 1
            else:
                return dfs(node.left, maxParentVal) + dfs(node.right, maxParentVal)
        return dfs(root, -101)

