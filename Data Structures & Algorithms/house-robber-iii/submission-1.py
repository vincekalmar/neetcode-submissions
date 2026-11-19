# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [0,0] #with root, without root
            
            left = dfs(node.left)
            right = dfs(node.right)

            withRoot = left[1] + right[1] + node.val
            withoutRoot = max(left) + max(right)

            return [withRoot, withoutRoot]

        return max(dfs(root))


        


        


