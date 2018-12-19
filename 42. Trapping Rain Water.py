class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # # Runtime: 144 ms, faster than 3.80% of Python online submissions for Trapping Rain Water.
        # self.cache_list = []
        # self.max = 0
        # self.water = 0
        # for position in height:
        #     if position <= self.max:
        #         for i in range(len(self.cache_list)):
        #             if position > self.cache_list[-i-1]:
        #                 self.water += position - self.cache_list[-i-1]
        #                 self.cache_list[-i-1] = position
        #             else:
        #                 break
        #         if position < self.max:
        #             self.cache_list.append(position)
        #         else:
        #             self.cache_list = [position]
        #     else:
        #         temp = self.max
        #         for i in range(len(self.cache_list)):
        #             self.water += temp - self.cache_list[-i-1]
        #         self.max = position
        #         self.cache_list = [position]
        #     # print('position:',position)
        #     # print(self.cache_list)
        #     # print('water:',self.water)
        # return self.water




a = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(a))