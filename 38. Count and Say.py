class Solution:
    adic = {1:'1'}
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Runtime: 40 ms, faster than 86.35% of Python3 online submissions for Count and Say.
        astr = '1'
        for index in range(n-1):
            p1 = 0
            p2 = 0
            emp_str = []
            while p2 < len(astr):
                if astr[p2] == astr[p1]:
                    p2 += 1
                    continue
                else:
                    emp_str.append(str(p2 - p1))
                    emp_str.append(str(astr[p1]))
                    p1 = p2
                    p2 += 1
            emp_str.append(str(p2 - p1))
            emp_str.append(str(astr[p1]))
            astr = ''.join(emp_str)
        return astr




for i in range(1,5):
    print(Solution().countAndSay(i))