class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Runtime: 20 ms, faster than 100.00% of Python online submissions for Two Sum II - Input array is sorted.
        dic = {}
        for i in range(len(numbers)):
            if (target - numbers[i]) in dic:
                return [dic[target - numbers[i]][1],i]
            else:
                dic[numbers[i]] = (numbers[i],i)




numbers = [4,7,11,2]
target = 9
print(Solution().twoSum(numbers, target))