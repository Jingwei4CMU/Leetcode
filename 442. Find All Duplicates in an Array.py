class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = set()
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                print(nums[i], i + 1, nums[nums[i] - 1])
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
            if nums[i] == i + 1:
                continue
            if nums[i] == nums[nums[i] - 1]:
                res.add(nums[i])
        return list(res)

a = [4,3,2,7,8,2,3,1]
print(Solution().findDuplicates(a))