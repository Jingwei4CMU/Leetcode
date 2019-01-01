from collections import Counter


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cout = Counter(nums)
        zeronums = cout[0]
        if zeronums >= 2:
            return [0] * len(nums)
        if zeronums == 1:
            to_return = [0 for i in range(len(nums) - 1)]
            result = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    result *= nums[i]
                else:
                    to_insert = i
            to_return.insert(to_insert, result)
            return to_return
        else:
            to_return = []
            result = 1
            for i in nums:
                result *= i
            for i in nums:
                to_return.append(result / i)
            return to_return



a = [1,0]
print(Solution().productExceptSelf(a))