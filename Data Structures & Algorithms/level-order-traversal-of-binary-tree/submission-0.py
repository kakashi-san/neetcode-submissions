# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = deque([root])
        res = []

        while q:
            level = [l.val for l in q]
            res.append(level)

            pop_len = len(q)

            for _ in range(pop_len):
                popped = q.popleft()

                if popped.left :
                    q.append(popped.left)

                if popped.right :
                    q.append(popped.right)

        return res