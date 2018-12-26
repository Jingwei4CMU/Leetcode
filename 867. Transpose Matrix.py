class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None:
            return None

        return [[A[col][row] for col in range(len(A))] for row in range(len(A[0]))]

#         row,col = len(A),len(A[0])
#         trans = [[None for i in range(row)]for j in range(col)]
#         for i in range(row):
#             for j in range(col):
#                 trans[j][i] = A[i][j]
#         return trans


