class Solution:

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime: 240 ms, faster than 79.69% of Python3 online submissions for Count Primes.
        if n < 2:
            return 0
        record = [1] * n
        record[0] = 0
        record[1] = 0

        m = 2
        while m * m < n:
            if record[m] == 1:
                record[m * m:n:m] = [0] * len(record[m * m:n:m])
            m += 1

        return sum(record)


print(Solution().countPrimes(10))