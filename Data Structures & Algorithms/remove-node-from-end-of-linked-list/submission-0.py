# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        list_size = 0
        curr = head
        while curr:
            list_size += 1
            curr = curr.next

        node_from_start = list_size - n 
        if node_from_start == 0:
            return head.next
        
        cnt = 1
        prev, curr = head, head.next
        while cnt != node_from_start:
            cnt += 1
            prev = prev.next
            curr = curr.next
        prev.next = curr.next

        return head