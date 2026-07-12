# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        first = preorder[0]

        idx = inorder.index(first)
        left_inorder = inorder[:idx]
        right_inorder = inorder[idx + 1:]

        left_preorder = preorder[1:len(left_inorder) + 1]
        right_preorder = preorder[len(left_inorder) + 1:]

        node = TreeNode(first)
        node.left = self.buildTree(left_preorder, left_inorder)
        node.right = self.buildTree(right_preorder, right_inorder)

        return node
