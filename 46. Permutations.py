class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            remain = nums[:i] + nums[i + 1:]
            temp = self.permute(remain)
            for j in temp:
                res.append([nums[i]] + j)
        return res

a = [1,2,3]
print(Solution().permute(a))