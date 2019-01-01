class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def checkone():
            for i in matrix:
                if '1' in i:
                    return True
            return False
        if checkone():
            temp = 1
        else:
            return 0
        height = len(matrix)
        width = len(matrix[0])
        while checkone():
            for i in range(height-temp):
                for j in range(width-temp):
                    if matrix[i][j] == '1':
                        if matrix[i+1][j+1] == '0' or matrix[i][j+1] == '0' or matrix[i+1][j] == '0':
                            matrix[i][j] = '0'
            for i in range(height):
                matrix[i][width-temp] = '0'
            for j in range(width):
                matrix[height-temp][j] = '0'

            temp += 1
        return (temp-1)**2


s =[["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
print(Solution().maximalSquare(s))