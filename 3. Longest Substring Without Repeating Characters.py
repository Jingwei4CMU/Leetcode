class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 80 ms, faster than 91.17% of Python3 online submissions for Longest Substring Without Repeating Characters.
        maxlength = 0
        substr = []
        start_position = 0
        for i in s:
            if i in substr:
                tempindex = substr.index(i)
                substr = substr[tempindex+1:]
                substr.append(i)
            else:
                substr.append(i)
                if len(substr) > maxlength:
                    maxlength = len(substr)
        return maxlength