class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Intersection of Two Arrays II.
        to_return = []
        dic = {}
        for i in nums1:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in nums2:
            if i in dic:
                if dic[i] > 0:
                    to_return.append(i)
                    dic[i] -= 1
                else:
                    del dic[i]
        return to_return