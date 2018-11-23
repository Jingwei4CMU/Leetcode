class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        adic = {}
        index = 0
        for num in nums:
            adic[num] = index
            index = index + 1
        for i in range(target+1):
            try:
                return [adic[i],adic[target-i]]
            except:
                pass


print(Solution().twoSum([1,2,3],5))

