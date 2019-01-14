class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = s.split(' ')[::-1]
        for i in range(len(temp) - 1, -1, -1):
            if temp[i] == '':
                temp.pop(i)
        if len(temp) == 0:
            return ''
        if len(temp) == 1:
            return temp[0]
        res = temp[0] + ' '
        for i in range(1, len(temp)):
            res += temp[i] + ' '
        return res[:-1]
s = ' d   g  '
print(Solution().reverseWords(s))