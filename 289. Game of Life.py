class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        hight = len(board)
        width = len(board[0])
        def cal_next(x,y):
            alive = 0
            for i in range(-1,2):
                if x+i < 0 or x+i > hight-1:
                    continue
                for j in range(-1,2):
                    if y+j < 0 or y+j > width-1 or (i == 0 and j == 0):
                        continue
                    alive += board[x+i][y+j]%10
                    print(i,j,alive)
            if board[x][y] == 1:
                if alive == 2 or alive == 3:
                    board[x][y] += 10
            else:
                if alive == 3:
                    board[x][y] += 10
        for i in range(hight):
            for j in range(width):
                cal_next(i,j)
        for i in range(hight):
            for j in range(width):
                board[i][j] = board[i][j]//10
        return board

b = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(Solution().gameOfLife(b))

