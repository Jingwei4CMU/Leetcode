class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # something wrong
        # if len(nums) <= 1:
        #     return len(nums)
        # else:
        #     deleted = 0
        #     for i in range(1, len(nums)):
        #         i = i - deleted
        #         if nums[i] == nums[i-1]:
        #             nums = nums[:i-1] + nums[i:]
        #             deleted += 1
        #     return len(nums)

        # Runtime: 56 ms, faster than 99.97% of Python3 online submissions for Remove Duplicates from Sorted Array.
        a=set(nums)
        length=len(a)
        nums.clear()
        for i in a:
            nums.append(i)
        nums.sort()
        return length




print(Solution().removeDuplicates([1, 1, 2]))


