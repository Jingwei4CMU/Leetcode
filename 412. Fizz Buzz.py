class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Runtime: 52 ms, faster than 98.61% of Python3 online submissions for Fizz Buzz.
        result = []
        for i in range(1,n+1):
            fizz = i % 3 == 0
            buzz = i % 5 == 0
            if not fizz and not buzz:
                result.append(str(i))
            elif fizz and buzz:
                result.append('FizzBuzz')
            elif fizz and not buzz:
                result.append('Fizz')
            elif buzz and not fizz:
                result.append('Buzz')
        return result



print(Solution().fizzBuzz(15))