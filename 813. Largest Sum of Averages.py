class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        res = [[float('-inf') for i in range(K + 1)] for j in range(len(A) + 1)]
        res[0][0] = 0
        dic = {}

        def avr(start, end):
            try:
                return dic[(start, end)]
            except:
                pass
            to_return = sum(A[start:end + 1]) / (end - start + 1)
            dic[(start, end)] = to_return
            return to_return

        for i in range(1, K+1):
            for j in range(i, i + len(A) - K + 1):
                for k in range(i - 1, j):
                    temp = res[i - 1][k] + avr(k, j - 1)
                    if temp > res[i][j]:
                        res[i][j] = temp
            print(res)
        return res[K][len(A)]

A = [9,1,2,3,9]
K = 3
print(Solution().largestSumOfAverages(A,K))