class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        flag = 0
        if k > 0:
            return len(set(nums) & set(i + k for i in nums))
        elif k == 0:
            return sum(i > 1 for i in collections.Counter(nums).values())

        else:
            return 0


