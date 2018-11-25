class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Runtime: 60 ms, faster than 56.33% of Python3 online submissions for Add Digits.
        while num >= 10:
            dig = len(str(num))
            temp = 0
            for i in range(dig):
                temp += num % 10
                num = num // 10
            num = temp
        return num




print(Solution().addDigits(58))