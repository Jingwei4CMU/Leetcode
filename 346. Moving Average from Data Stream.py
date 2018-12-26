class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        # Runtime: 56 ms, faster than 100.00% of Python3 online submissions for Moving Average from Data Stream.
        self.list = []
        self.window = size
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.list) == self.window:
            self.sum -= self.list.pop(0)
        self.sum += val
        self.list.append(val)
        return self.sum / len(self.list)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)