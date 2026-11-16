# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        dummy = ListNode(-1, head) #-1
        slow = fast = head #-1

        # find middle of the list

        while fast.next and fast.next.next:
            slow = slow.next #2 4
            fast = fast.next.next #4 8

        second = slow.next
        slow.next = None

        # reverse second half
        dum = None
        while second:
            temp = second.next
            second.next = dum
            dum = second
            second = temp

        
        # merge first and second lists
        # dummy is for first, dum is for second, dummy, dum, dummy, dum

        curr1 = dummy.next
        curr2 = dum

        while curr1 and curr2:
            temp1 = curr1.next
            temp2 = curr2.next

            curr1.next = curr2
            curr2.next = temp1

            curr1 = temp1
            curr2 = temp2


        




