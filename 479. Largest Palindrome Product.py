class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        finishwhen = 1
        bigest = 0
        for i in range(10 ** n - 1, 1, -1):
            if i < finishwhen:
                break
            for j in range(10 ** n - 1, i - 1, -1):
                if i*j > bigest:
                    if self.checkPalindrome(i * j):
                        bigest = i*j
                        finishwhen = i*j/(10 ** n - 1)
        print(bigest)
        return bigest%1337

    def checkPalindrome(self, n):
        if n == 0:
            return True
        # nlist = []
        # while n > 0:
        #     nlist.append(n % 10)
        #     n = n // 10
        # if nlist == nlist[::-1]:
        #     return True
        # else:
        #     return False
        temp = str(n)
        if temp == temp[::-1]:
            return True
        else:
            return False

print(Solution().largestPalindrome(7))