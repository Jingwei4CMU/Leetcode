class Solution:
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lenA = len(A)
        dic = {}
        def dp(start,s):
            try:
                return dic[(start,s)]
            except:
                pass
            if start == lenA-1:
                return 1
            if s == 1:
                temp = A[start+1:]
                bigtemp = [i for i in temp if i >= A[start]]
                if bigtemp:
                    res = dp(start+1+temp.index(min(bigtemp)),2)
                    dic[(start,s)] = res
                    return res
                else:
                    dic[(start,s)] = 0
                    return 0
            else:
                temp = A[start+1:]
                smalltemp = [i for i in temp if i <= A[start]]
                if smalltemp:
                    res = dp(start+1+temp.index(max(smalltemp)),1)
                    dic[(start,s)] = res
                    return res
                else:
                    dic[(start,s)] = 0
                    return 0
        res = 0
        for i in range(len(A)):
            res += dp(i,1)
        print(dic)
        return res

A = [14,13,15]
print(Solution().oddEvenJumps(A))