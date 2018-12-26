class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return -1
        leftsum = 0
        temp = nums.pop(0)
        rightsum = sum(nums)
        for i in range(len(nums)):
            if leftsum == rightsum:
                return i
            leftsum += temp
            temp = nums.pop(0)
            rightsum -= temp
        if leftsum == rightsum:
            return i + 1
        else:
            return -1

