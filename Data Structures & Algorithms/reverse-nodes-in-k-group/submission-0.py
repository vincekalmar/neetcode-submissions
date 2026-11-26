# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
       
        left = right = head
        first = True
        while right:

            for i in range(k-1):
                right = right.next
                if not right: break
            if not right: break
            if not first:
                newTail.next = right
            prev = right.next
            # 0, 1->4. 1, 2->.1, 2 3->2, temp 4, prev 3
            newTail = left
            for i in range(k):
                temp = left.next
                left.next = prev
                prev = left
                left = temp
            
            if first:
                head = prev
                first = False
            right = left
        return head

            