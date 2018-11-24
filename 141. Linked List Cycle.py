# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Runtime: 48 ms, faster than 48.82% of Python online submissions for Linked List Cycle.
        adic = {}
        if head:
            while head.next:
                if adic.get(head) == 0:
                    return True
                adic[head] = 0
                head = head.next
        return False