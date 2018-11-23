# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # # Runtime: 48 ms, faster than 69.90% of Python3 online submissions for Merge Two Sorted Lists.
        # l3 = None
        # flag1 = l1
        # flag2 = l2
        # while flag1 and flag2:
        #     if flag1.val <= flag2.val:
        #         if l3:
        #             flag3.next = ListNode(flag1.val)
        #             flag3 = flag3.next
        #             flag1 = flag1.next
        #         else:
        #             l3 = ListNode(flag1.val)
        #             flag1 = flag1.next
        #             flag3 = l3
        #     else:
        #         if l3:
        #             flag3.next = ListNode(flag2.val)
        #             flag3 = flag3.next
        #             flag2 = flag2.next
        #         else:
        #             l3 = ListNode(flag2.val)
        #             flag2 = flag2.next
        #             flag3 = l3
        # while flag1:
        #     if l3:
        #         flag3.next = ListNode(flag1.val)
        #         flag3 = flag3.next
        #         flag1 = flag1.next
        #     else:
        #         l3 = ListNode(flag1.val)
        #         flag1 = flag1.next
        #         flag3 = l3
        # while flag2:
        #     if l3:
        #         flag3.next = ListNode(flag2.val)
        #         flag3 = flag3.next
        #         flag2 = flag2.next
        #     else:
        #         l3 = ListNode(flag2.val)
        #         flag2 = flag2.next
        #         flag3 = l3
        #
        #
        # return l3

        if None in (l1, l2):
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next,l1)
            return l2



l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

print(Solution().mergeTwoLists(l1,l2))

