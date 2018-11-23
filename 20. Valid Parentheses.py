class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
          """
        adic = {'(':')','{':'}','[':']'}
        s = list(s)
        plist = []
        while s:
            if plist == []:
                if s[0] in ['(','[','{']:
                    plist = [s.pop(0)]
                else:
                    return False
            elif adic[plist[-1]] == s[0]:
                s.pop(0)
                plist.pop()
            else:
                if s[0] in ['}',']',')']:
                    return False
                plist.append(s.pop(0))
        if plist == []:
            return True
        else:
            return False









print(Solution().isValid("()[]{}"))