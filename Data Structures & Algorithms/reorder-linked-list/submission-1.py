# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next


        curr2 = slow.next
        slow.next = None

        dummy = None

        while curr2:
            temp = curr2.next
            curr2.next = dummy
            dummy = curr2
            curr2 = temp

        curr2 = dummy
        curr1 = head

        while  curr1 and curr2:
            temp1 = curr1.next
            temp2 = curr2.next

            curr1.next = curr2
            curr2.next = temp1

            curr1 = temp1
            curr2 = temp2








