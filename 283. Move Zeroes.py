class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # # Runtime: 592 ms, faster than 5.29% of Python3 online submissions for Move Zeroes.
        # try:
        #     p1 = nums.index(0)
        #     p2 = p1 + 1
        #     while p2 < len(nums):
        #         if nums[p2] == 0:
        #             p2 += 1
        #         else:
        #             nums[p1] = nums[p2]
        #             nums[p2] = 0
        #             p1 = nums.index(0)
        #             p2 += 1
        # except:
        #     pass


        # Runtime: 48 ms, faster than 94.85% of Python3 online submissions for Move Zeroes.
        lengthn = len(nums)
        i = 0
        while i < lengthn:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                lengthn -= 1
                continue
            i += 1




print(Solution().moveZeroes(nums=[0, 1, 0, 3, 12]))