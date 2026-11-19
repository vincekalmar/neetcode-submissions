# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
     #  1, 2, 3, 4, 5, 6, 7 n =3 
     #              l        r  
        dummy = ListNode(-1, head)
        l = dummy
        r = head

        for _ in range(n):
            r = r.next

        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return dummy.next



