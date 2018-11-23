class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
          """
        # # Runtime: 40 ms, faster than 56.52% of Python3 online submissions for Valid Parentheses.
        # adic = {'(':')','{':'}','[':']'}
        # s = list(s)
        # plist = []
        # while s:
        #     if plist == []:
        #         if s[0] in ['(','[','{']:
        #             plist = [s.pop(0)]
        #         else:
        #             return False
        #     elif adic[plist[-1]] == s[0]:
        #         s.pop(0)
        #         plist.pop()
        #     else:
        #         if s[0] in ['}',']',')']:
        #             return False
        #         plist.append(s.pop(0))
        # if plist == []:
        #     return True
        # else:
        #     return False

        # # Runtime: 52 ms, faster than 22.74% of Python3 online submissions for Valid Parentheses.
        # while s:
        #     s_s = s.replace('()','').replace('[]','').replace('{}','')
        #     if s_s == s:
        #         return False
        #     else:
        #         s = s_s
        # return True

        # # Runtime: 40 ms, faster than 56.52% of Python3 online submissions for Valid Parentheses.
        # s = list(s)
        # adic = {'(': ')', '{': '}', '[': ']'}
        # plist = []
        # while s:
        #     if s[0] in ['(','[','{']:
        #         plist.append(s.pop(0))
        #     else:
        #         if plist == []:
        #             return False
        #         else:
        #             if adic[plist[-1]] == s[0]:
        #                 s.pop(0)
        #                 plist.pop()
        #             else:
        #                 return False
        # if plist == []:
        #     return True
        # else:
        #     return False

        # Runtime: 36 ms, faster than 98.78% of Python3 online submissions for Valid Parentheses.
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                top_element = stack.pop() if stack else '#'
                if mapping[ch] != top_element:
                    return False
        if stack:
            return False
        else:
            return True











print(Solution().isValid("()[]{}"))