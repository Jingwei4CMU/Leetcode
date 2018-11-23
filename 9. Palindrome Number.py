class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # # Runtime: 260 ms, faster than 93.75% of Python3 online submissions for Palindrome Number.
        # xstring = str(x)
        # slen = len(xstring) - 1
        # for i in range(len(xstring) // 2):
        #     if xstring[i] != xstring[slen - i]:
        #         return False
        # return True


        # # Runtime: 256 ms, faster than 96.85% of Python3 online submissions for Palindrome Number.
        # if x < 0:
        #     return False
        # xstring = str(x)
        # slen = len(xstring) - 1
        # for i in range(len(xstring) // 2):
        #     if xstring[i] != xstring[slen - i]:
        #         return False
        # return True

        # However, this problem is not allowed to convert integer to string

        ##
        # This method is convert the second half part of the integer and compare with the first half.
        # 348 ms, faster than 48.01% of Python3 online submissions for Palindrome Number.
        if x<0 or (x%10 == 0 and x != 0):
            return False
        renum = 0
        while x > renum:
            renum = renum*10 + x%10
            x = x//10

        return x == renum or x == renum//10



print(Solution().isPalindrome(-12321))