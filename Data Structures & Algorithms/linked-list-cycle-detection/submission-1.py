# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        dummy = ListNode(0, head)

        fast = slow = dummy
        
        while fast.next != None and slow != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast.val == slow.val:
                return True
        return False