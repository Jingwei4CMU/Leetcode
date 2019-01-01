class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """

        def dp(start, end, pick):

            guess = (start + end) // 2
            if guess == pick:
                return 0
            if guess > pick:
                result1 = guess + dp(start, guess - 1, pick)
                return result1
            if guess < pick:
                result2 = guess + dp(guess + 1, end, pick)
                return result2
        need = 0
        for i in range(1, n + 1):
            temp = dp(1, n, i)
            if temp > need:
                need = temp
        return need
n = 5
print(Solution().getMoneyAmount(n))