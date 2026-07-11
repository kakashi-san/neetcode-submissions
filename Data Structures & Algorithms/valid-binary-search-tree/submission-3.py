# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_list = []

        def traverse(node):
            if not node:
                return 
            traverse(node.left)
            inorder_list.append(node.val)
            traverse(node.right)

        traverse(root)

        for i in range(len(inorder_list) - 1):
            if inorder_list[i] >= inorder_list[i + 1]:
                return False
        
        return True