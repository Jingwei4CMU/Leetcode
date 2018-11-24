class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # # Runtime: 44 ms, faster than 90.09% of Python3 online submissions for Best Time to Buy and Sell Stock.
        # if len(prices) > 2:
        #     diff_list = []
        #     for i in range(1, len(prices)):
        #         diff_list.append(prices[i] - prices[i - 1])
        #     for i in range(1, len(diff_list)):
        #         if diff_list[i - 1] > 0:
        #             diff_list[i] += diff_list[i - 1]
        #     return max(max(diff_list), 0)
        # elif len(prices) == 2:
        #     if prices[0] < prices[1]:
        #         return prices[1] - prices[0]
        #     else:
        #         return 0
        # else:
        #     return 0

        minprice = 100000000
        maxpro = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i]-minprice>maxpro:
                maxpro = prices[i]-minprice
        return maxpro



print(Solution().maxProfit([2,1,5]))