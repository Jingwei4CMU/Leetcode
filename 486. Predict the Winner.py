class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}

        def dp(start, end, player, diff):
            try:
                return dic[(start, end, player, diff)]
            except:
                pass
            if start > end:
                if diff >= 0:
                    dic[(start, end, player, diff)] = True
                    return True
                else:
                    dic[(start, end, player, diff)] = False
                    return False
            if player == 1:
                temp = dp(start + 1, end, 2, diff + nums[start]) or dp(start, end - 1, 2, diff + nums[end])
                dic[(start, end, player, diff)] = temp
                return temp
            else:
                temp = dp(start + 1, end, 1, diff - nums[start]) and dp(start, end - 1, 1, diff - nums[end])
                dic[(start, end, player, diff)] = temp
                return temp

        return dp(0, len(nums) - 1, 1, 0)
a = [1, 5, 233, 7]
print(Solution().PredictTheWinner(a))