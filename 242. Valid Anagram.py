class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Runtime: 72 ms, faster than 50.14% of Python3 online submissions for Valid Anagram.
        if sorted(s) == sorted(t):
            return True
        else:
            return False