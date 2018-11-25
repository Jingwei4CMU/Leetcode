# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Runtime: 56 ms, faster than 80.77% of Python3 online submissions for Diameter of Binary Tree.
        self.cal_max_depth(root)
        node_list = [root]
        longest_path = 0
        while len(node_list) != 0:

            if node_list[0].left:
                node_list.append(node_list[0].left)
            if node_list[0].right:
                node_list.append(node_list[0].right)

            left_depth = node_list[0].left.val if node_list[0].left != None else 0
            right_depth = node_list[0].right.val if node_list[0].right != None else 0

            if left_depth + right_depth > longest_path:
                longest_path = left_depth + right_depth
            node_list.pop(0)
        return longest_path


    def cal_max_depth(self, root):
        if root.left == None and root.right == None:
            root.val = 1
            return root.val
        rightval = self.cal_max_depth(root.right) if root.right != None else 0
        leftval = self.cal_max_depth(root.left) if root.left != None else 0
        root.val = max(rightval + 1, leftval + 1)
        return root.val





root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

Solution().diameterOfBinaryTree(root=root)
print(root.val)