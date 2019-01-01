# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root.val = root
        todo = [root]
        while todo:
            thisnode = todo.pop(0)
            if thisnode.left:
                thisnode.left.val = (thisnode,0)
                todo.append(thisnode.left)
            if thisnode.right:
                thisnode.left.val = (thisnode,0)
                todo.append(thisnode.right)
        def havezero():
            todo = [root]
            while todo:
                thisnode = todo.pop(0)
                if thisnode.val[1] == 0:
                    return True
                if thisnode.left:
                    todo.append(thisnode.left)
                if thisnode.right:
                    todo.append(thisnode.right)
            return False
        round = 0
        while havezero():
            #spread
            # find all leaves
            leaves = []
            todo = [root]
            while todo:
                thisnode = todo.pop(0)
                if thisnode.left:
                    if thisnode.left.val[1] == 1:
                        leftnone = True
                    else:
                        leftnone = False
                else:
                    leftnone = True
                if thisnode.right:
                    if thisnode.right.val[1] == 1:
                        rightnone = True
                    else:
                        rightnone = False
                else:
                    rightnone = True
                if leftnone and rightnone:
                    leaves.append(thisnode)
                if thisnode.left:
                    todo.append(thisnode.left)
                if thisnode.right:
                    todo.append(thisnode.right)

            # parent and grandparent to 1
            for i in leaves:
                i.val[0].val[1] = 1
                i.val[0].val[0].val[1] = 1
            round += 1
        return round
