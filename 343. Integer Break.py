class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod = [1, 1, 2]
        if n <= 3:
            return prod[n - 1]
        prod = [1, 2, 3]
        for i in range(3, n):
            prod.append(max([prod[j] * prod[i - j - 1] for j in range(i // 2 + 1)]))
        return prod[n - 1]

print(Solution().integerBreak(10))