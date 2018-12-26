# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime: 32 ms, faster than 99.93% of Python3 online submissions for First Bad Version.
        p1 = 1
        p2 = n
        while p1 <= p2:
            p3 = (p1+p2)//2
            if isBadVersion(p3):
                p2 = p3 - 1
            else:
                p1 = p3 + 1
        return p1