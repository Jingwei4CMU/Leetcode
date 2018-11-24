class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Runtime: 40 ms, faster than 99.81% of Python3 online submissions for Add Binary.
        return bin(int(a, 2)+int(b, 2))[2:]


print(Solution().addBinary(a = "11", b = "1"))