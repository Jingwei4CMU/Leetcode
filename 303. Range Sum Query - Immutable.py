class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.dic = {}

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        try:
            return self.dic[(i, j)]
        except:
            pass
        if i == j:
            self.dic[(i, j)] = self.nums[i]
            return self.nums[i]
        if i + 1 <= j - 1:
            temp = self.sumRange(i - 1, j - 1)
            self.dic[(i, j)] = temp + self.nums[i] + self.nums[j]
            self.dic[(i, j - 1)] = temp + self.nums[i]
            self.dic[(i + 1, j)] = temp + self.nums[j]
        else:
            temp = sum(self.nums[i:j + 1])
            self.dic[(i, j)] = temp
        return self.dic[(i, j)]

# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(0,2)
print(param_1)