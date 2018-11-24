# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 76 ms, faster than 98.40% of Python3 online submissions for Remove Linked List Elements.
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        if head == None:
            return []
        p1 = head
        while p1.next:
            if p1.next.val == val:
                p1.next = p1.next.next
            else:
                p1 = p1.next

        return head