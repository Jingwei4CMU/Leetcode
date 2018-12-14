from collections import defaultdict
class Solution:
    # Runtime: 108 ms, faster than 32.18% of Python3 online submissions for Number of Islands.
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.mark_dict = {}
        for i in range(len(grid)):
            self.mark_dict[i] = defaultdict(int)

        self.island_found = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.mark_dict[i][j] == 0 and grid[i][j] == '1':
                    self.island_found += 1
                    self.mark_island(i, j, self.island_found,grid)
        print(self.mark_dict)
        return self.island_found



    def mark_island(self,i,j,mark,grid):
        self.mark_dict[i][j] = mark
        # check left

        if i-1 >= 0 and i-1 < len(grid) and j >=0 and j<len(grid[0]):
            temp_island = grid[i-1][j]
            temp_mark = self.mark_dict[i-1][j]
            if temp_mark == 0 and temp_island == '1':
                self.mark_island(i-1, j, mark,grid)

        if i+1 >= 0 and i+1 < len(grid) and j >=0 and j<len(grid[0]):
            temp_island = grid[i+1][j]
            temp_mark = self.mark_dict[i+1][j]
            if temp_mark == 0 and temp_island == '1':
                self.mark_island(i+1, j, mark,grid)

        if i >= 0 and i < len(grid) and j-1 >=0 and j-1<len(grid[0]):
            temp_island = grid[i][j-1]
            temp_mark = self.mark_dict[i][j-1]
            if temp_mark == 0 and temp_island == '1':
                self.mark_island(i, j-1, mark,grid)

        if i >= 0 and i < len(grid) and j+1 >=0 and j+1<len(grid[0]):
            temp_island = grid[i][j+1]
            temp_mark = self.mark_dict[i][j+1]
            if temp_mark == 0 and temp_island == '1':
                self.mark_island(i, j+1, mark,grid)

# island = [[00000],[00000],[00000],[00000]]
island = [['1','1','1','0','0'],['1','1','1','1','1'],['0','0','0','0','0'],['0','0','0','0','1']]
print(Solution().numIslands(island))