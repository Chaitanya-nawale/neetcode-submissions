# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        result = ListNode(0)
        curr = result
        while l1 and l2:
            next_val = l1.val + l2.val + remainder
            curr.next = ListNode( next_val % 10)
            remainder = next_val // 10
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            if remainder != 0:
                next_val = l1.val + remainder
                curr.next = ListNode( next_val % 10)
                remainder = next_val // 10
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next
        while l2:
            if remainder != 0:
                next_val = l2.val + remainder
                curr.next = ListNode( next_val % 10)
                remainder = next_val // 10
                curr = curr.next
                l2 = l2.next
            else:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next
        while remainder:
            curr.next = ListNode( remainder % 10)
            remainder = remainder // 10
        return result.next
        
