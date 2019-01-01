class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        rs = [amount+1] * (amount+1)
        print(rs)
        rs[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i-c] + 1)
                    print(rs)

        if rs[amount] == amount+1:
            return -1
        return rs[amount]


coins = [1,2,5]
amount = 11
print(Solution().coinChange(coins,amount))