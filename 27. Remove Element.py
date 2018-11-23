class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Runtime: 40 ms, faster than 69.26% of Python3 online submissions for Remove Element.
        numlen = len(nums)
        if val not in nums:
            return numlen
        pointer_slow = 0
        for pointer_fast in range(numlen):
            if nums[pointer_fast] != val:
                nums[pointer_slow] = nums[pointer_fast]
                pointer_slow += 1
        return pointer_slow






print(Solution().removeElement(nums = [0,1,2,2,3,0,4,2],val = 2))