# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preIdx = inIdx = 0

        def dfs(boundary):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder) or inIdx >= len(inorder):
                return None
            if boundary == inorder[inIdx]:
                inIdx += 1
                return None
            




            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(boundary)
            return root

        return dfs(-1001)
