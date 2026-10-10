"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        og_list_ptr = head
        while og_list_ptr:
            new_node = Node(og_list_ptr.val)
            new_node.next = og_list_ptr.next
            og_list_ptr.next = new_node
            og_list_ptr = new_node.next

        og_list_ptr = head
        while og_list_ptr:
            if og_list_ptr.random:
                og_list_ptr.next.random = og_list_ptr.random.next
            og_list_ptr = og_list_ptr.next.next
        
        new_list_ptr = head.next
        og_list_ptr = head
        while og_list_ptr:
            cp_node = og_list_ptr.next
            og_list_ptr.next = cp_node.next
            if cp_node.next:
                cp_node.next = cp_node.next.next
            og_list_ptr = og_list_ptr.next

        return new_list_ptr