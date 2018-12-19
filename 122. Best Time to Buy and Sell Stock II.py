class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Runtime: 24 ms, faster than 98.44% of Python online submissions for Best Time to Buy and Sell Stock II.
        if not prices:
            return 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] >= prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit





price = [7,1,5,3,6,4]
print(Solution().maxProfit(price))