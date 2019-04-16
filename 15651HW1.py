import math
def MultiMedian(a,nums):
    aim = int(math.log2(a))
    res = []
    while aim >= 0:
        subaim = 2**aim-1
        temp = []
        while True:
            print(nums)
            print(subaim)
            big = []
            small = []
            for i in nums[1:]:
                if i > nums[0]:
                    big.append(i)
                if i < nums[0]:
                    small.append(i)
            print('small',small)
            if len(small) == subaim:
                res.insert(0,nums[0])
                temp += small
                break
            elif len(small) > subaim:
                nums = small
            else:
                temp += small
                temp += [nums[0]]
                nums = big
                subaim -= len(small)+1
        nums = temp
        aim -= 1
    return len(res)-1, res


nums = [3,2,1]
a = len(nums)
print(MultiMedian(a,nums))


