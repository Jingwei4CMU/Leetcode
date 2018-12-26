class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        basket = []
        categories = []
        maxget = 0
        tempget = 0
        for i in tree:
            if len(categories) == 2:
                if i in categories:
                    tempget += 1
                    if basket[-1][0] == i:
                        temp = basket.pop()
                        temp = (i,temp[1]+1)
                        basket.append(temp)
                    else:
                        basket.append((i,1))
                else:
                    prevget = basket[-1]
                    basket = [prevget,(i,1)]
                    categories = [prevget[0],i]
                    tempget = sum(j for i, j in basket)

            elif len(categories) == 1:
                tempget += 1
                if i in categories:
                    temp = basket.pop()
                    temp = (i,temp[1]+1)
                    basket.append(temp)
                else:
                    categories.append(i)
                    basket.append((i,1))
            else:
                tempget += 1
                categories.append(i)
                basket.append((i,1))

            # temp = sum(j for i,j in basket)
            if tempget > maxget:
                maxget = tempget
        return maxget

a = [3,3,3,1,2,1,1,2,3,3,4]
print(Solution().totalFruit(a))