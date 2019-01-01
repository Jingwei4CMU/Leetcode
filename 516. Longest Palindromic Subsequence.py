class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=1:
            return len(s)
        n = len(s)-1
        res = [[0 for i in range(n+1)]for i in range(n+1)]
        for i in range(n+1):
            res[i][i] = 1
        lenth = 1
        print(res)
        while lenth < n+1:
            print(res)
            for i in range(n+1-lenth):
                j = i + lenth
                if s[i] == s[j]:
                    res[i][j] = max(res[i+1][j], res[i][j-1], res[i+1][j-1]+2)
                else:
                    res[i][j] = max(res[i+1][j], res[i][j-1])
            lenth += 1
        return res[0][n]

s = "eabcbab"
print(Solution().longestPalindromeSubseq(s))