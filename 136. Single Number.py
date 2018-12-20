from collections import defaultdict


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # Runtime: 48 ms, faster than 16.29% of Python online submissions for Single Number.
        # dic = defaultdict(int)
        # for i in nums:
        #     dic[i] += 1
        # for i in dic.keys():
        #     if dic[i] == 1:
        #         return i

        # return 2 * sum(set(nums)) - sum(nums)

        result = 0
        for num in nums:
            result = result ^ num
            print(result)
        return result

a = [2,2,1]
print(Solution().singleNumber(a))