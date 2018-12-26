# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # Runtime: 96 ms, faster than 83.11% of Python3 online submissions for Merge Two Binary Trees.
        if t1 or t2:
            nt = TreeNode(None)
            return self.merge(nt, t1, t2)
        else:
            return None

    def merge(self, nt, t1, t2):
        # merge root
        if t1 or t2:
            val1 = t1.val if t1 else 0
            val2 = t2.val if t2 else 0
            nt.val = val1 + val2
        else:
            return nt
        # merge left
        templeftnode1 = t1.left if t1 else None
        templeftnode2 = t2.left if t2 else None
        if templeftnode1 or templeftnode2:
            tempnode = TreeNode(None)
            nt.left = self.merge(tempnode, templeftnode1, templeftnode2)
        # merge right
        temprightnode1 = t1.right if t1 else None
        temprightnode2 = t2.right if t2 else None
        if temprightnode1 or temprightnode2:
            tempnode = TreeNode(None)
            nt.right = self.merge(tempnode, temprightnode1, temprightnode2)
        return nt


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # Runtime: 80 ms, faster than 100.00% of Python3 online submissions for Merge Two Binary Trees.
        if t1 and t2:
            t1.val = t1.val + t2.val
        else:
            return t1 or t2
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1












