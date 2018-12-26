class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Runtime: 40 ms, faster than 100.00% of Python3 online submissions for Happy Number.
        dic = {}
        while n != 1:
            if n in dic or n == 0:
                return False
            dic[n] = 1
            newn = 0
            while n > 0:
                newn += (n%10)**2
                n = n//10
            n = newn
        return True