# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root is not None and root.left is None and root.right is None:
            return 1
        else:
            max_depth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
            return max_depth