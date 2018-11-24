# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # # Runtime: 44 ms, faster than 64.23% of Python3 online submissions for Reverse Linked List.
        # if head:
        #     node_list = []
        #     while head:
        #         node_list.append(head)
        #         head = head.next
        #     if node_list:
        #         new_head = node_list.pop()
        #         flag1 = new_head
        #     while node_list:
        #         flag1.next = node_list.pop()
        #         flag1 = flag1.next
        #     flag1.next = None
        #     return new_head
        # else:
        #      return head

        # Runtime: 40 ms, faster than 99.25% of Python3 online submissions for Reverse Linked List.
        if head:
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        else:
            return None



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


print(Solution().reverseList(head=head).next.next.next.next.val)