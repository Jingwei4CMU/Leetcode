class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        type1 = [i for i in range(len(s))]
        sum1 = len(type1)
        n = 0
        while type1:
            n += 1
            nexttype1 = []
            for i in type1:
                if i-n >=0 and i+n <= len(s)-1:
                    if s[i-n] == s[i+n]:
                        nexttype1.append(i)
            type1 = nexttype1
            sum1 += len(type1)

        type2 = []
        sum2 = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                type2.append(i)
        sum2 += len(type2)

        n = 0
        while type2:
            n += 1
            nexttype2 = []
            for i in type2:
                if i-n >= 0 and i+1+n <= len(s)-1:
                    if s[i-n] == s[i+1+n]:
                        nexttype2.append(i)
            type2 = nexttype2
            sum2 += len(type2)
        return sum1 + sum2

s = 'aaa'
print(Solution().countSubstrings(s))
