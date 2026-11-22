# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxSum = -float('inf')
        def dfs(node):
            nonlocal maxSum
            if not node:
                return -float('inf')
            
            left = dfs(node.left)
            right = dfs(node.right)
          #  print("node ", node.val, " left, right", left, ' ', right)
            maxSum = max(maxSum, left + node.val, right+ node.val, node.val, left+right + node.val, left, right)

            return max(left + node.val, right+ node.val, node.val)
        
        dfs(root)
        return maxSum

      