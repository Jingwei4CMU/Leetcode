# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Runtime: 76 ms, faster than 83.65% of Python online submissions for Palindrome Linked List.
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        # length = len(temp)//2
        # if temp[:length] == temp[::-1][:length]:
        #     return True
        # else:
        #     return False
        p1 = 0
        p2 = len(temp)-1
        while p1 < p2:
            if temp[p1] != temp[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True


