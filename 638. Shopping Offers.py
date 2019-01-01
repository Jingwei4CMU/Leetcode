class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        def need2str(list):
            return ''.join([str(i) + '#' for i in list])
        def str2need(s):
            return [int(i) for i in s.split('#')[:-1]]

        dic = {}
        needsc = need2str(needs)
        def dp(needsc):
            try:
                return dic[needsc]
            except:
                pass
            newneed = str2need(needsc)
            if sum([i!=0 for i in newneed])==0:
                dic[needsc] = 0
                return 0
            if sum([i<0 for i in newneed]) > 0:
                dic[needsc] = float('inf')
                return float('inf')
            result = float('inf')
            for sale in special:
                temp = newneed.copy()
                for i,pic in enumerate(sale[:-1]):
                    temp[i] -= pic
                result = min(result, sale[-1]+dp(need2str(temp)))
            for i,goodprice in enumerate(price):
                temp = newneed.copy()
                temp[i] -= 1
                result = min(result, goodprice+dp(need2str(temp)))
            dic[needsc] = result
            return result
        return dp(needsc)

price = [5,6,1,2,10,3]
special =[[6,5,3,3,1,4,17],[0,6,5,0,1,2,3],[4,1,5,6,4,1,2],[3,1,2,4,2,2,6]]
needs =[6,3,2,5,0,5]
print(Solution().shoppingOffers(price, special, needs))