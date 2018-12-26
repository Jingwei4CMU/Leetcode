# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dig(root, 0)

    def dig(self, root, depth):
        if root:
            return max(self.dig(root.left, depth + 1), self.dig(root.right, depth + 1))
        else:
            return depth
