# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        head = None 
        curr = None
        prev = None
        carry = 0

        while l1 or l2:
            if not l1: val = l2.val + carry
            elif not l2: val = l1.val + carry
            else: val = l1.val + l2.val + carry

            num = val % 10
            carry = val // 10

            if not head:
                head = ListNode(num)
                curr = head
                prev = curr
                curr.next = ListNode()
                curr = curr.next
            else:
                curr.val = num
                prev = curr
                curr.next = ListNode()
                curr = curr.next
            print(prev.val)

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry:
            curr.val = 1
        else:
            prev.next = None
        return head

            
