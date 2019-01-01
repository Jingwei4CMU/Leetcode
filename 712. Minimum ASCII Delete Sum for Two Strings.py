class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        len1 = len(s1)
        len2 = len(s2)
        res = [[0 for i in range(len2+1)] for j in range(len1+1)]
        s1 += '~'
        s2 += '~'
        for i in range(len1-1,-1,-1):
            for j in range(len2-1,-1,-1):
                if s1[i+1] == s2[j+1]:
                    res[i][j] = min(res[i+1][j]+ord(s1[i+1]), res[i][j+1]+ord(s2[j+1]), res[i+1][j+1])
                else:
                    res[i][j] = min(res[i+1][j]+ord(s1[i+1]), res[i][j+1]+ord(s2[j+1]))
        for i in range(97,97+26):
            print(chr(i))
            print(i)
        return res[0][0]

s1 = "sea"
s2 = "eat"
print(Solution().minimumDeleteSum(s1,s2))