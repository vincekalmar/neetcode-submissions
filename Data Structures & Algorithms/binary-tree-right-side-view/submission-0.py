# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = deque()
        res = []

        q.append(root)
        
        while q:

            n = len(q)

            for i in range(n):
                curr = q.popleft()
                if curr:
                    if i==0:
                        res.append(curr.val)
                    if curr.right:
                        q.append(curr.right)
                    if curr.left:
                        q.append(curr.left)

        return res
        