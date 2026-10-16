# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        node_list = [root]
        while node_list:
            temp = node_list[0].left
            node_list[0].left = node_list[0].right
            node_list[0].right = temp
            if node_list[0].right:
                node_list.append(node_list[0].right)
            if node_list[0].left:  
                node_list.append(node_list[0].left)
            node_list.pop(0)
        return root  
        