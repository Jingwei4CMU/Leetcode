class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Runtime: 168 ms, faster than 13.54% of Python online submissions for Add Strings.
        to_return = 0
        depth = 1

        for i in num1[::-1]:
            to_return += (ord(i)-48) * depth
            depth *= 10
        depth = 1
        for i in num2[::-1]:
            to_return += (ord(i)-48) * depth
            depth *= 10
        result = ''
        if to_return == 0:
            return "0"
        while to_return > 0:
            result += chr(to_return%10+48)
            to_return = to_return // 10
        return result[::-1]




str1 = "0"
str2 = "0"
print(Solution().addStrings(str1,str2))