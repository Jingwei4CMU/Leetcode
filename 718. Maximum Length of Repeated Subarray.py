class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        lena = len(A)
        lenb = len(B)
        res = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
        for i in range(lena - 1, -1, -1):
            for j in range(lenb - 1, -1, -1):
                if A[i] == B[j]:
                    res[i][j] = res[i + 1][j + 1] + 1
                else:
                    res[i][j] = 0
        print(res)
        return res[0][0]


A = [4,1,2,3,2,1,5]
B = [1,2,3,2,2,4]
print(Solution().findLength(A,B))