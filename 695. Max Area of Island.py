from collections import defaultdict
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        hight = len(grid)
        width = len(grid[0])
        dic = defaultdict(int)
        maxarea = 0
        def cal_area(x,y):
            if dic[(x,y)] == 1:
                return 0
            dic[(x,y)] = 1
            if x<0 or x>hight-1 or y<0 or y>width-1:
                return 0
            if grid[x][y] == 0:
                return 0
            res = 1
            res += cal_area(x-1,y)
            res += cal_area(x+1,y)
            res += cal_area(x,y-1)
            res += cal_area(x,y+1)
            return res
        for i in range(hight):
            for j in range(width):
                temp = cal_area(i,j)
                maxarea = max(maxarea,temp)
        return maxarea

a = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(Solution().maxAreaOfIsland(a))