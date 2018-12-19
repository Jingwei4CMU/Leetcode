import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string.ascii_lowercase
        # Runtime: 36 ms, faster than 95.27% of Python online submissions for Valid Palindrome.
        if len(s) == 0:
            return True
        for i in string.punctuation:
            s = s.replace(i, '')
        s = s.replace(' ', '')
        print(s)
        if len(s) <= 1:
            return True
        s = s.lower()
        li = 0
        ri = len(s)-1
        while li <= ri:
            if s[li] == s[ri]:
                li += 1
                ri -= 1
            else:
                return False
        return True



a = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(a))