class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or k == 0:
            return False
        dic = {}
        for i in range(k+1):
            if i == len(nums):
                return False
            if nums[i] in dic:
                return True
            dic[nums[i]] = 1
        p1, p2 = 0, k+1
        while p2 < len(nums):
            print('p2:',p2)
            print(dic)
            del dic[nums[p1]]
            if nums[p2] in dic:
                return True
            dic[nums[p2]] = 1
            p1 += 1
            p2 += 1
        return False

a = [1,0,1,1]
k = 1
print(Solution().containsNearbyDuplicate(a,k))