# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []
            for index in range(0, len(lists), 2):
                list_1 = lists[index]
                if index + 1 < len(lists):
                    list_2 = lists[index + 1]
                else:
                    list_2 = None
                
                merged_lists.append(self.merge_two_lists(list_1, list_2))
            lists = merged_lists
            
        return lists[0]

    def merge_two_lists(self, list_1: Optional[ListNode], list_2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        prev = head

        while list_1 and list_2:
            if list_1.val < list_2.val:
                prev.next = list_1
                list_1 = list_1.next
            else:
                prev.next = list_2
                list_2 = list_2.next
            prev = prev.next

        if list_1:
            prev.next = list_1
        else:
            prev.next = list_2

        return head.next