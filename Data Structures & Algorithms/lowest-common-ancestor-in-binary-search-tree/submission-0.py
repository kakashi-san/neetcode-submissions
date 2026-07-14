# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def rec(node, target):
            if not node:
                return None
            
            if node.val == target:
                return [node.val]
            
            left_node = rec(node.left, target)
            if left_node is not None:
                left_node.append(node.val)
                return left_node

            right_node = rec(node.right, target)

            if right_node is not None:
                right_node.append(node.val)
                return right_node

            return 

        p_list = rec(root, p.val)
        p_list = p_list

        q_list = rec(root, q.val)
        q_list = q_list

        for val in p_list:
            if val in q_list:
                return TreeNode(val)
 