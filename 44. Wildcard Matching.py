class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        i, j = 0, 0
        istar, jstar = -1, -1 # meaning no star yet

        while i < len(s):
            print(i,j,istar,jstar)
            if j < len(p) and (p[j] == '?' or p[j] == s[i]):
                print('a')
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                print('b')
                istar, jstar = i, j
                j += 1
            elif istar != -1:
                print('c')
                i, j = istar + 1, jstar + 1
                istar += 1
            else:
                return False
            print(i, j, istar, jstar)
            print('---------')

        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)


s = 'abcdabcd'
p = 'a*cd'
print(Solution().isMatch(s,p))