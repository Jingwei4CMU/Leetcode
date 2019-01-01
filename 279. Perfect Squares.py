# class Solution:
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         # Time Limit Exceeded
#         dic = {0:0}
#         for i in range(1,n+1):
#             temp = i
#             for j in range(1,i+1):
#                 prev = i-j**2
#                 if prev in dic:
#                     temp = min(temp,dic[prev]+1)
#                 else:
#                     break
#             dic[i] = temp
#             # print(dic)
#         return dic[n]
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = {0: 0, 1: 1,2:2,3:3}

        def subprob(n):
            try:
                return dic[n]
            except:
                pass
            result = []
            for i in range(int(n ** 0.5 // 1), 0, -1):
                to_check = n - i ** 2
                if to_check >= 0:
                    result.append(subprob(to_check) + 1)
            to_return = min(result)
            dic[n] = to_return
            return to_return

        return subprob(n)


print(Solution().numSquares(3102))