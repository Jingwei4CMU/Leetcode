class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # p1 = 0
        # for p2 in range(1, len(nums)):
        #     if nums[p1] > 0:
        #         if nums[p2] > 0:
        #             nums[p1] *= nums[p2]
        #         else:
        #             p1 += 1
        #             nums[p1] = nums[p2]
        #     elif nums[p1] < 0:
        #         p1 += 1
        #         nums[p1] = nums[p2]
        #     else:
        #         if nums[p2] != 0:
        #             p1 += 1
        #             nums[p1] = nums[p2]
        # nums = nums[:p1+1]
        # print(nums)
        # dic = {}
        #
        # def submax(left, right):
        #     try:
        #         return dic[(left,right)]
        #     except:
        #         pass
        #     if left > right:
        #         dic[(left,right)] = float('-inf')
        #         return float('-inf')
        #     if left == right:
        #         return nums[left]
        #     print('check',left,right)
        #     negindexs = [i+left for i, j in enumerate(nums[left:right + 1]) if j < 0]
        #     if len(negindexs)%2 == 0:
        #         prod = 1
        #         for i in nums[left:right+1]:
        #             prod *= i
        #         dic[(left, right)] = prod
        #         return prod
        #     result1 = submax(left,negindexs[0]-1)
        #     result2 = submax(negindexs[0]+1,right)
        #     if len(negindexs) == 1:
        #         tempresult = max(result1,result2)
        #         dic[(left, right)] = tempresult
        #         return tempresult
        #     result3 = submax(left,negindexs[-1]-1)
        #     result4 = submax(negindexs[-1]+1,left)
        #     tempresult = max(result1,result2,result3,result4)
        #     dic[(left,right)] = tempresult
        #     return tempresult
        #
        # if 0 in nums:
        #     result = float('-inf')
        #     indexs = [i for i, j in enumerate(nums) if j == 0]
        #     left = 0
        #     while indexs:
        #         right = indexs.pop(0)
        #         result = max(result, submax(left, right - 1))
        #         left = right + 1
        #     right = len(nums) - 1
        #     result = max(result, submax(left, right))
        #     if result < 0:
        #         return 0
        #     return result
        #
        # else:
        #     left = 0
        #     right = len(nums) - 1
        #     return submax(left, right)
        B = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(nums + B)

a = [1,2,3,0,-1,-10,-2,0]
print(Solution().maxProduct(a))
