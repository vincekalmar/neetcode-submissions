# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        slow = ListNode(-1, head)
        fast = head

        while fast and fast.next and fast.next.next:
            if slow.val == fast.val:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False