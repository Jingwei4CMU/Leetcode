class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1

        n = len(nums)
        if n <= 2:
            return n

        count = 2
        target = nums[1]
        state = 'down' if nums[1] > nums[0] else 'up'

        # print(nums)
        for i in range(2, n):
            if state == 'down':
                if nums[i] < target:
                    count += 1
                    state = 'up'
            elif state == 'up':
                if nums[i] > target:
                    count += 1
                    state = 'down'
            target = nums[i]
        return count

a = [1,17,5,10,13,15,10,5,16,8]
print(Solution().wiggleMaxLength(a))