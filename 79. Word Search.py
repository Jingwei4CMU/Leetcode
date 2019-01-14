from collections import defaultdict


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        hight = len(board)
        width = len(board[0])

        def subp(x, y, start, dic):

            if start > len(word) - 1:
                return True
            if x < 0 or x > hight - 1 or y < 0 or y > width - 1:
                return False
            if dic[(x, y)]:
                return False
            if board[x][y] == word[start]:
                # print(x, y, word[start:])
                dic[(x, y)] = True
                res = False
                res = res or subp(x - 1, y, start + 1, dic.copy())
                if res:
                    return True
                res = res or subp(x + 1, y, start + 1, dic.copy())
                if res:
                    return True
                res = res or subp(x, y - 1, start + 1, dic.copy())
                if res:
                    return True
                res = res or subp(x, y + 1, start + 1, dic.copy())
                if res:
                    return True
                return False
            else:
                return False

        for i in range(hight):
            for j in range(width):
                dic = defaultdict(bool)
                temp = subp(i, j, 0, dic)
                if temp:
                    return True
        return False

b = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
w = "ABCESEEEFS"
print(Solution().exist(b,w))