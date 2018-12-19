class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
    #     # Runtime: 852 ms, faster than 0.92% of Python online submissions for Find All Anagrams in a String.
    #     result = []
    #     start = 0
    #     lasttrue = 0
    #     while start <= len(s) - len(p):
    #         if start > len(s)-len(p)+1:
    #             break
    #         if lasttrue == 1:
    #             lastletter = s[start-1]
    #         else:
    #             lastletter = ''
    #         temp = self.check_ana(s[start:start+len(p)], p, lasttrue, lastletter)
    #         if temp == True:
    #             result.append(start)
    #             lasttrue = 1
    #         else:
    #             lasttrue = 0
    #             if temp >= 0:
    #                 start = start + temp
    #         start += 1
    #     return result
    #
    # def check_ana(self,s,p,lasttrue, lastletter):
    #     temp_p = list(p)
    #     if lasttrue == 1:
    #         if s[-1] == lastletter:
    #             return True
    #         elif s[-1] not in p:
    #             return len(s)-1
    #         else:
    #             return -1
    #     for i in s:
    #         if i not in p:
    #             return s.index(i)
    #         try:
    #             temp_p.remove(i)
    #         except:
    #             return -1
    #     return True
        key = [0]*26
        temp = [0] * 26
        to_return = []
        for j in p:
            key[ord(j)-97] += 1
        n = len(p)
        for i,j in enumerate(s):
            temp[ord(j) - 97] += 1
            if i >= n:
                temp[ord(s[i-n])-97] -= 1
            if temp == key:
                to_return.append(i-n+1)
        return to_return




s = "abcdabc"
p = "abc"
print(Solution().findAnagrams(s,p))
