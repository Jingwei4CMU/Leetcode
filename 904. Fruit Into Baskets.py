# class Solution(object):
#     def totalFruit(self, tree):
#         """
#         :type tree: List[int]
#         :rtype: int
#         """
#         basket = []
#         categories = []
#         maxget = 0
#         tempget = 0
#         for i in tree:
#             if len(categories) == 2:
#                 if i in categories:
#                     tempget += 1
#                     if basket[-1][0] == i:
#                         temp = basket.pop()
#                         temp = (i,temp[1]+1)
#                         basket.append(temp)
#                     else:
#                         basket.append((i,1))
#                 else:
#                     prevget = basket[-1]
#                     basket = [prevget,(i,1)]
#                     categories = [prevget[0],i]
#                     tempget = sum(j for i, j in basket)
#
#             elif len(categories) == 1:
#                 tempget += 1
#                 if i in categories:
#                     temp = basket.pop()
#                     temp = (i,temp[1]+1)
#                     basket.append(temp)
#                 else:
#                     categories.append(i)
#                     basket.append((i,1))
#             else:
#                 tempget += 1
#                 categories.append(i)
#                 basket.append((i,1))
#
#             # temp = sum(j for i,j in basket)
#             if tempget > maxget:
#                 maxget = tempget
#         return maxget

class Solution:
    def totalFruit(self, tree: 'List[int]') -> 'int':
        maxget = 0
        res = 0
        last = None
        prev = None
        lastnum = 0
        for i in tree:
            if i == last:
                lastnum += 1
                maxget += 1
            elif i == prev:
                lastnum = 1
                prev, last = last, prev
                maxget += 1
            else:
                maxget = lastnum
                maxget += 1
                prev, last = last, i
                lastnum = 1
            if maxget > res:
                res = maxget
        return res


a = [5,0,0,7,0,7,2,7]
print(Solution().totalFruit(a))