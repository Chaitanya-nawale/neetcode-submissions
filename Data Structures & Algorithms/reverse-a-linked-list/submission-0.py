# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            if head.next:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            else:
                head.next = prev
                break
        return head


            