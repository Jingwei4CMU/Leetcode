class MinStack:
    # Runtime: 56 ms, faster than 99.36% of Python3 online submissions for Min Stack.
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min != []:
            if x < self.min[-1]:
                self.min.append(x)
        else:
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack[-1] == self.min[-1]:
            if not self.min[-1] in self.stack[:-1]:
                self.min.pop()
            return self.stack.pop()
        else:
            return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()