class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # # Runtime: 56 ms, faster than 28.82% of Python3 online submissions for Implement strStr().
        # if needle:
        #     start_letter = needle[0]
        #     search_list = [i for i, e in enumerate(haystack) if e == start_letter]
        #     find = -1
        #     needlen = len(needle)
        #     for i in search_list:
        #         try:
        #             if haystack[i:i + needlen] == needle:
        #                 return i
        #         except:
        #             pass
        #     return find
        #
        # else:
        #     return 0

        # Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Implement strStr().

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        if needle:
            return -1
        else:
            return 0





print(Solution().strStr(haystack="a", needle="a"))