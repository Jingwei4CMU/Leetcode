from collections import defaultdict
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # # Runtime: 492 ms, faster than 0.94% of Python online submissions for Isomorphic Strings.
        # d1 = defaultdict(int)
        # d2 = defaultdict(int)
        # flag1 = 0
        # flag2 = 0
        # for i in range(len(s)):
        #     if d1[s[i]] == 0:
        #         flag1 += 1
        #         d1[s[i]] = flag1
        #     if d2[t[i]] == 0:
        #         flag2 += 1
        #         d2[t[i]] = flag2
        #     print(d1[s[i]],d2[t[i]])
        #     if d1[s[i]] != d2[t[i]]:
        #         return False
        # return True

        # Runtime: 52 ms, faster than 30.19% of Python online submissions for Isomorphic Strings.
        d = defaultdict(int)
        d2 = defaultdict(int)
        for i in range(len(s)):
            if d[t[i]] == 0 and d2[s[i]] == 0:
                d[t[i]] = s[i]
                d2[s[i]] = t[i]
            elif d[t[i]] != s[i] or d2[s[i]] != t[i]:
                return False
        return True


s = 'egg'
t = 'abb'
print(Solution().isIsomorphic(s,t))