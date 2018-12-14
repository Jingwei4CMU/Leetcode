# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    # Runtime: 68 ms, faster than 98.16% of Python online submissions for Copy List with Random Pointer.
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # copy with one linked list
        if head == None:
            return None
        lold = head
        while lold:
            temp_node = RandomListNode(lold.label)
            lold.next, temp_node.next = temp_node, lold.next
            lold = temp_node.next

        # copy random pointers
        lold = head
        while lold:
            try:
                lold.next.random = lold.random.next
            except:
                pass
            lold = lold.next.next

        # seperate old and new
        lnew = RandomListNode(0)
        temp_node = lnew
        lold = head
        while lold:
            temp_node.next = lold.next
            temp_node = temp_node.next
            lold.next = temp_node.next
            lold = temp_node.next
        return lnew.next






