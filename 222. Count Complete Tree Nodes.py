# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 1  # to count the root

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: # if empty it will return 0
            return 0
        if root.left:
            self.count += 1
            self.countNodes(root.left)
        if root.right:
            self.count += 1
            self.countNodes(root.right)
        return self.count
