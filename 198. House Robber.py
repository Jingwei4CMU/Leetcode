class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        pre_money = nums[0]
        curr_money = max(nums[:2])
        print(pre_money, curr_money)
        for i in range(2,len(nums)):
            m = nums[i]
            temp = curr_money
            curr_money = max(pre_money + m, curr_money)
            pre_money = temp
            print(pre_money,curr_money)
        return curr_money

a = [1,1,1,2]
print(Solution().rob(a))