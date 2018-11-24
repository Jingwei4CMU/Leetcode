class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # # Runtime: 40 ms, faster than 55.29% of Python3 online submissions for Search Insert Position.
        # p1 = 0
        # p2 = len(nums)-1
        # while p2 - p1 > 1:
        #     p3 = (p2+p1)//2
        #     if nums[p3] == target:
        #         return p3
        #     elif nums[p3] > target:
        #         p2 = p3
        #     else:
        #         p1 = p3
        # if target <= nums[p1]:
        #     return p1
        # elif target <= nums[p2]:
        #     return p2
        # else:
        #     return p2 + 1


        # # Runtime: 40 ms, faster than 55.29% of Python3 online submissions for Search Insert Position.
        # if target > nums[-1]:
        #     return len(nums)
        # elif target < nums[0]:
        #     return 0
        # for i in range(max(nums)):
        #     try:
        #         return nums.index(target+i)
        #     except:
        #         pass

        # Runtime: 36 ms, faster than 98.00% of Python3 online submissions for Search Insert Position.
        p1 = 0
        p2 = len(nums)-1
        while p1 <= p2:
            p3 = (p2+p1)//2
            if nums[p3] == target:
                return p3
            elif nums[p3] > target:
                p2 = p3-1
            else:
                p1 = p3+1
        return p1




print(Solution().searchInsert([1,3,5,6], 2))