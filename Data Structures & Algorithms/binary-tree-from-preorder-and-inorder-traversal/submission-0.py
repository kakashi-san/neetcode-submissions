class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        first = preorder[0]
        inorder_idx = inorder.index(first)

        inorder_left = inorder[:inorder_idx]
        inorder_right = inorder[inorder_idx + 1:]

        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]

        node = TreeNode(first)
        node.left = self.buildTree(preorder_left, inorder_left)
        node.right = self.buildTree(preorder_right, inorder_right)

        return node