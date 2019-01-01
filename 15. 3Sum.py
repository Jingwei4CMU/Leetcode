class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2:
            return None
        prevset = set(nums[:2])
        result = []
        dic = {}
        dic[sum(nums[:2])] = [nums[:2]]
        for i in range(2, len(nums)):
            print(dic)
            if -nums[i] in dic:
                for toadd in dic[-nums[i]]:
                    toadd.append(nums[i])
                    temptoadd = sorted(toadd)
                    if temptoadd not in result:
                        result.append(temptoadd)
            for previtem in nums[:i]:
                if previtem + nums[i] not in dic:
                    dic[previtem + nums[i]] = [[previtem, nums[i]]]
                else:
                    dic[previtem + nums[i]].append([previtem, nums[i]])
        return result

a = [0,0,0,0]
print(Solution().threeSum(a))