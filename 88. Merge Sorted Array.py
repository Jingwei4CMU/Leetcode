class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # # Runtime: 36 ms, faster than 99.84% of Python3 online submissions for Merge Sorted Array.
        # p1 = m-1
        # p2 = n-1
        # p3 = m+n-1
        # while p1>=0 and p2>=0:
        #     if nums1[p1] >= nums2[p2]:
        #         nums1[p3] = nums1[p1]
        #         p1 -= 1
        #     else:
        #         nums1[p3] = nums2[p2]
        #         p2 -= 1
        #     p3 -= 1
        # if p2 >= 0:
        #     nums1[:p2+1] = nums2[:p2+1]
        # return nums1

        # Runtime: 36 ms, faster than 99.84% of Python3 online submissions for Merge Sorted Array.
        nums1[m:] = nums2
        nums1[:] = sorted(nums1)





print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))