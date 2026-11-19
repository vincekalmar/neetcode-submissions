"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        
        ogToNew = {}

        curr = head

        while curr:
            ogToNew[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            clone = ogToNew[curr]
            
            cloneNext = curr.next
            if not cloneNext: clone.next = None
            else: clone.next = ogToNew[cloneNext]
          
            cloneRandom = curr.random
            if not cloneRandom: clone.random = None
            else: clone.random = ogToNew[cloneRandom]

            curr = curr.next

        return ogToNew[head]