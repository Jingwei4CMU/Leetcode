class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sumn = sum(nums)
        if sumn%k != 0:
            return False
        aim = sumn/k
        nums = sorted(nums)[::-1]
        if nums[0]>aim:
            return False
        res = [0 for i in range(k)]
        for i in range(len(nums)):
            if nums[i] == 0:
                break
            res[res.index(min(res))] += nums[i]
        print(res)
        for i in res:
            if i != aim:
                return False
        return True

nums = [2,2,10,5,2,7,2,2,13]
k = 3
print(Solution().canPartitionKSubsets(nums,k))