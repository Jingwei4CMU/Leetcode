class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 136 ms, faster than 70.28% of Python3 online submissions for Roman to Integer.
        s = s.replace('IV','E')
        s = s.replace('IX','F')
        s = s.replace('XL','G')
        s = s.replace('XC','H')
        s = s.replace('CD','K')
        s = s.replace('CM','P')
        return s.count('M') * 1000 + s.count('D') * 500 + \
               s.count('C') * 100 + s.count('L') * 50 + \
               s.count('X') * 10 + s.count('V') * 5 + \
               s.count('I') * 1 + \
               s.count('E') * 4 + s.count('F') * 9 + \
               s.count('G') * 40 + s.count('H') * 90 + \
               s.count('K') * 400 + s.count('P') * 900





print(Solution().romanToInt("MCMXCIV"))