class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: Runtime: 108 ms, faster than 80.06% of Python3 online submissions for First Unique Character in a String.
        sset = []
        for i in range(len(s)):
            if s[i] not in sset:
                sset.append(s[i])
                if not s[i] in s[i+1:]:
                    return i
        return -1






print(Solution().firstUniqChar("loveleetcode"))