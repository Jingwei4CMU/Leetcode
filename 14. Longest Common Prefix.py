class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # # Runtime: 64 ms, faster than 14.33% of Python3 online submissions for Longest Common Prefix.
        # if len(strs) == 0:
        #     return ""
        # for i in range(1, len(strs[0])+1):
        #     for j in range(1,len(strs)):
        #         if strs[0][:i] == strs[j][:i]:
        #             continue
        #         else:
        #             return strs[0][:i-1]
        # return strs[0]





print(Solution().longestCommonPrefix([]))