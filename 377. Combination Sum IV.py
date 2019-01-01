class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dic = {}
        nums = sorted(nums)
        def dp(n):
            try:
                return dic[n]
            except:
                pass
            if n < 0:
                dic[n] = 0
                return 0
            if n == 0:
                dic[n] = 1
                return 1
            result = 0
            for i in nums:
                temp = dp(n-i)
                result += temp
            dic[n] = result
            return result
        return dp(target)

nums = [4,2,1]
target = 32
print(Solution().combinationSum4(nums, target))