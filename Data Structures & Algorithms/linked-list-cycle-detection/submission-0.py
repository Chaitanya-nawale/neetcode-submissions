# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr_len = 0
        while head:
            if curr_len >= 1001:
                return True
            head = head.next
            curr_len += 1
        return False