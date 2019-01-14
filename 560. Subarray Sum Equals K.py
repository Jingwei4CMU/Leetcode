class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        if nums[0] == 0:
            dic[0] = [-1,0]
        else:
            dic[0] = [-1]
            dic[nums[0]] = [0]
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
        res = 0
        print(dic,nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] - k in dic:
                res += len([j for j in dic[nums[i] - k] if j < i])
        return res

a = [0]
k = 0
print(Solution().subarraySum(a,k))