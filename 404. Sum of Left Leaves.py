class Solution:
    def __init__(self):
        self.sums = 0

    def helper(self, root, child_type):
        if root is None:
            return
        if child_type == "left" and root.left is None and root.right is None:
            self.sums += root.val
        self.helper(root.left, "left")
        self.helper(root.right, "right")

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.helper(root, "type")
        return self.sums
