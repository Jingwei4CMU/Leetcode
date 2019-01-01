class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) <= 1:
            return nums
        nums = sorted(nums)
        # print(nums)
        maxlen = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            # print('i:',i,nums[i])
            for j in range(i):
                # print('j:', j,nums[j])
                if nums[i] % nums[j] == 0:
                    if maxlen[j] + 1 > maxlen[i]:
                        maxlen[i] = maxlen[j] + 1
                        # print(maxlen)
        # print(maxlen)
        big = nums[maxlen.index(max(maxlen))]
        to_return = []
        start = 1
        for i in range(len(nums)):
            if nums[i] == big:
                to_return.append(nums[i])
                break
            if big%nums[i] == 0:
                if maxlen[i] == start:
                    to_return.append(nums[i])
                    start += 1
        return to_return

nums = [2,3,4,9,8]
print(Solution().largestDivisibleSubset(nums))