class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # # Runtime: 40 ms, faster than 97.16% of Python3 online submissions for Jewels and Stones.
        # if J and S:
        #     result = 0
        #     for i in J:
        #         result += S.count(i)
        #     return result
        # else:
        #     return 0

        Jset = set(J)
        return sum([i in Jset for i in S])