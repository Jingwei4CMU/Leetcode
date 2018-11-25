class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # # Runtime: 68 ms, faster than 22.96% of Python3 online submissions for Intersection of Two Arrays.
        # return list(set([i for i in nums1 if i in nums2]))

        # Runtime: 40 ms, faster than 82.71% of Python3 online submissions for Intersection of Two Arrays.
        result = []
        set1 = set(nums1)
        set2 = set(nums2)
        for i in set1:
            if i in set2:
                result.append(i)
        return result


print(Solution().intersection(nums1 = [1,2,2,1], nums2 = [2,2]))