from collections import defaultdict
class MaxStack:
    # # Runtime: 212 ms, faster than 16.29% of Python3 online submissions for Max Stack.
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stack_list = []
    #
    #
    # def push(self, x):
    #     """
    #     :type x: int
    #     :rtype: void
    #     """
    #     self.stack_list.append(x)
    #
    # def pop(self):
    #     """
    #     :rtype: int
    #     """
    #     try:
    #         return self.stack_list.pop(-1)
    #     except:
    #         return None
    #
    #
    # def top(self):
    #     """
    #     :rtype: int
    #     """
    #     try:
    #         return self.stack_list[-1]
    #     except:
    #         return None
    #
    # def peekMax(self):
    #     """
    #     :rtype: int
    #     """
    #     if self.stack_list:
    #         return max(self.stack_list)
    #     else:
    #         return None
    #
    # def popMax(self):
    #     """
    #     :rtype: int
    #     """
    #     if self.stack_list:
    #         temp_max = self.stack_list[0]
    #         temp_index = 0
    #         for i in range(len(self.stack_list)):
    #             if self.stack_list[i] >= temp_max:
    #                 temp_index = i
    #                 temp_max = self.stack_list[i]
    #         return self.stack_list.pop(temp_index)
    #     else:
    #         return None








    # # Runtime: 164 ms, faster than 57.20% of Python3 online submissions for Max Stack.
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stack_list = []
    #     self.order_list = []
    #
    # def push(self, x):
    #     """
    #     :type x: int
    #     :rtype: void
    #     """
    #     self.stack_list.append(x)
    #
    #     start_index = 0
    #     end_index = len(self.order_list)-1
    #     while(start_index <= end_index):
    #         temp_index = (start_index+end_index)//2
    #         if self.order_list[temp_index] > x:
    #             end_index = temp_index - 1
    #         elif self.order_list[temp_index] < x:
    #             start_index = temp_index + 1
    #         else:
    #             self.order_list.insert(temp_index, x)
    #             return None
    #     self.order_list.insert(start_index, x)
    #
    #
    #
    #
    # def pop(self):
    #     """
    #     :rtype: int
    #     """
    #     temp_pop = self.stack_list.pop()
    #     self.order_list.pop(self.order_list.index(temp_pop))
    #     return temp_pop
    #
    #
    # def top(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.stack_list[-1]
    #
    #
    # def peekMax(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.order_list[-1]
    #
    #
    # def popMax(self):
    #     """
    #     :rtype: int
    #     """
    #     temp_pop = self.order_list.pop()
    #     temp_list = self.stack_list[::-1]
    #     temp_list.pop(temp_list.index(temp_pop))
    #     self.stack_list = temp_list[::-1]
    #     return temp_pop

    #  Runtime: 364 ms, faster than 3.41% of Python3 online submissions for Max Stack.
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_list = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        temp_list = [x, self.stack_list[-1][-1] if self.stack_list else None]
        self.stack_list.append((x, max([i for i in temp_list if i is not None])))


    def pop(self):
        """
        :rtype: int
        """
        return self.stack_list.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        return self.stack_list[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.stack_list[-1][-1]

    def popMax(self):
        """
        :rtype: int
        """
        to_return = self.stack_list[-1][-1]
        temp_list = []
        while self.stack_list[-1][0] != to_return:
            temp_list.append(self.stack_list.pop())
        self.stack_list.pop()
        print(temp_list)
        for item in reversed(temp_list):
            self.push(item[0])
        return to_return




# Your MaxStack object will be instantiated and called as such:
obj = MaxStack()
obj.push(5)
obj.push(1)
obj.push(5)
print('list:',obj.stack_list)
print(obj.pop())
print('list:',obj.stack_list)
print(obj.popMax())
print('list:',obj.stack_list)
print(obj.top())