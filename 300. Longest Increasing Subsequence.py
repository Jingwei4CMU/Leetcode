#class Solution:
#     def lengthOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         dic = {}
#         end = len(nums)
#
#         def dp(prev, start):
#             try:
#                 if start in dic:
#                     p,m = dic[start]
#                     if p >= prev:
#                         return m
#             except:
#                 pass
#             if start == end:
#                 return 0
#             result0 = dp(prev, start + 1)
#             if nums[start] > prev:
#                 # take this num
#                 result1 = 1 + dp(nums[start], start + 1)
#             else:
#                 dic[start] = (prev, result0)
#                 return result0
#             result = max(result0, result1)
#             dic[start] = (prev, result)
#             # print(dic)
#             return result
#
#         return dp(float('-inf'), 0)
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j] and result[j] + 1 > result[i]:
                    result[i] = result[j] + 1
            print(result)

        return max(result)


a = [1,3,6,7,9,4,10,5,6]
print(Solution().lengthOfLIS(a))