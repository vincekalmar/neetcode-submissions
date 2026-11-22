# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        minHeap = []
        for node in lists:
            if node:
                node = Node(node)
                minHeap.append(node)

        heapq.heapify(minHeap)

        head = ListNode(0)
        curr = head

        while minHeap:
            wrapped = heapq.heappop(minHeap)
            curr.next = wrapped.node
            curr = curr.next
            if wrapped.node.next:
                heapq.heappush(minHeap, Node(wrapped.node.next))
        
        return head.next


        





