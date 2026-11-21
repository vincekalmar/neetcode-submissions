"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        clones = {}
        q = deque()
        q.append(node)
        clones[node] = Node(node.val)
        seen = set()
        seen.add(node)
        while q:
            curr = q.popleft()
            clone = clones[curr]

            for nei in curr.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)

                cloneNei = clones[nei]
                clone.neighbors.append(cloneNei)
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)


        return clones[node]



        