class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic1 = {0:'I',1:'X',2:'C',3:'M'}
        dic4 = {0:'IV',1:'XL',2:'CD'}
        dic5 = {0:'V',1:'L',2:'D'}
        dic9 = {0:'IX',1:'XC',2:'CM'}
        level = 0
        digit = num % 10
        num = num // 10
        res = ''
        while num != 0 or digit != 0:
            temp = ''
            if digit == 4:
                temp += dic4[level]
            elif digit == 9:
                temp += dic9[level]
            elif digit < 4:
                temp += dic1[level] * int(digit)
            else:
                temp += dic5[level]
                temp += dic1[level] * int(digit-5)
            level += 1
            res = temp + res
            digit = num % 10
            num = num // 10
            print(num, digit)
        return res

num = 10
print(Solution().intToRoman(num))