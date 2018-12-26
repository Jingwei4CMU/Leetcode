class Solution(object):
    def isStrobogrammatic(self, num):
           return set(map(operator.add, num, num[::-1])) <= set('69 96 00 11 88'.split())


# class Solution(object):
#     def isStrobogrammatic(self, num):
#         """
#         :type num: str
#         :rtype: bool
#         """
#         dic = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
#         for i in range(len(num)//2+1):
#             try:
#                 if dic[num[i]] == num[len(num)-i-1]:
#                     continue
#                 else:
#                     return False
#             except:
#                 return False
#         return True