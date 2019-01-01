class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dic = {}
        end = len(prices)

        def subprob(start):
            try:
                return dic[start]
            except:
                pass
            width = end - start
            if width <= 1:
                dic[start] = 0
                return 0
            buy = float('inf')
            sell = float('-inf')
            for i in range(start, end):
                if sell > buy and prices[i] < sell:
                    break
                if prices[i] <= buy:
                    buy = prices[i]
                else:
                    if prices[i] >= sell:
                        sell = prices[i]
                        prevsell = prices[i - 1]
                        sellday = i
            if sell == float('-inf'):
                return 0
            profit = sell - buy
            futureprofit = subprob(sellday + 2)
            preprofit = prevsell - buy
            if preprofit > 0:
                otherprofit = subprob(sellday + 1)
                tempresult = max(profit + futureprofit, preprofit + otherprofit)
                dic[start] = tempresult
                return tempresult
            else:
                tempresult = profit + futureprofit
                dic[start] = tempresult
                return tempresult

        return subprob(0)

p = [6,1,3,2,4,7]
print(Solution().maxProfit(p))