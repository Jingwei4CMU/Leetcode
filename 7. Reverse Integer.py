class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # # Runtime: 56 ms, faster than 79.26% of Python3 online submissions for Reverse Integer.
        #
        # xlist = list(str(abs(x)))
        # result = ''
        # xlen = len(xlist)
        # for i in range(xlen):
        #     result = result + xlist[xlen - i - 1]
        # result = int(result)
        #
        # if (result > 2 ** 31 - 1) or (result < -2 ** 31):
        #     return 0
        # if x < 0:
        #     return -result
        # else:
        #     return result


        #  52 ms, faster than 99.36% of Python3 online submissions for Reverse Integer.


        xstring = str(abs(x))
        result = ''
        xlen = len(xlist)
        for i in range(xlen):
            result = result + xstring[xlen - i - 1]
        result = int(result)

        if (result > 2 ** 31 - 1) or (result < -2 ** 31):
            return 0
        if x < 0:
            return -result
        else:
            return result





print(Solution().reverse(1534236469))