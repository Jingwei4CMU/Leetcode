class Solution:
    adic = {1:1,2:2}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        try:
            return Solution.adic[n]
        except:
            result = self.climbStairs(n-1) + self.climbStairs(n-2)

            Solution.adic[n] = result
            return result










print(Solution().climbStairs(100))