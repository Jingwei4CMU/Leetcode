class Solution(object):
    def circularArrayLoop(self, nums):
        N = len(nums)
        for i, jump in enumerate(nums):
            nums[i] = jump % N if jump > 0 else -jump % N * -1

        def nextindex(i):
            jump = nums[i]
            if jump > 0:
                return (i + jump) % N
            elif jump < 0:
                return (-i - jump) % N * -1
            else:
                return 0

        for i, jump in enumerate(nums):
            if jump != 0:
                slow = fast = i
                slow, fast = nextindex(slow), nextindex(nextindex(fast))
                while nums[slow] * nums[fast] > 0:
                    if slow == fast: return True
                    slow, fast = nextindex(slow), nextindex(nextindex(fast))
                slow = i
                while nums[slow]:
                    nums[slow] = 0
                    slow = nextindex(slow)
        return False

nums = [1, 2, 5, 7, 8, 7, 6]
print(Solution().circularArrayLoop(nums))