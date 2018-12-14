# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
#
# class Solution(object):
#     # Runtime: 4200 ms, faster than 8.84% of Python online submissions for Merge k Sorted Lists.
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         deleted = 0
#         for i in range(len(lists)):
#             if lists[i - deleted] == None:
#                 lists.pop(i - deleted)
#                 deleted += 1
#         if len(lists) == 1:
#             return lists[0]
#         elif len(lists) == 0:
#             return None
#         head_nodes = [i.val for i in lists]
#         start_index = head_nodes.index(min(head_nodes))
#         start_node = lists[start_index]
#         lists.remove(start_node)
#         for list2add in lists:
#             temp_node = start_node
#             while list2add and temp_node.next:
#                 if list2add.val <= temp_node.next.val:
#                     new_node = ListNode(list2add.val)
#                     new_node.next = temp_node.next
#                     temp_node.next = new_node
#                     temp_node = temp_node.next
#                     list2add = list2add.next
#                 else:
#                     temp_node = temp_node.next
#             if list2add:
#                 temp_node.next = list2add
#         return start_node


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Runtime: 80 ms, faster than 58.09% of Python online submissions for Merge k Sorted Lists.
        deleted = 0
        for i in range(len(lists)):
            if lists[i - deleted] == None:
                lists.pop(i - deleted)
                deleted += 1
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 0:
            return None
        to_return = []
        for one_list in lists:
            while one_list:
                to_return.append(one_list.val)
                one_list = one_list.next
        to_return.sort()

        head = dumnhead = ListNode(None)
        for one in to_return:
            head.next = ListNode(one)
            head = head.next
        return dumnhead.next


