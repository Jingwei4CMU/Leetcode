class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # Runtime: 36 ms, faster than 99.58% of Python3 online submissions for Backspace String Compare.
        S = list(S)
        while S[0] == '#':
            S.pop(0)
        lens = len(S)
        i = 0
        while i < lens:
            if S[i] == '#':
                S.pop(i)
                if i > 0:
                    S.pop(i - 1)
                    i -= 1
                    lens -= 1
                lens -= 1
                continue
            i += 1

        T = list(T)
        while T[0] == '#':
            T.pop(0)
        lens = len(T)
        i = 0
        while i < lens:
            if T[i] == '#':
                T.pop(i)
                if i > 0:
                    T.pop(i - 1)
                    i -= 1
                    lens -= 1
                lens -= 1
                continue
            i += 1
        if T == S:
            return True
        else:
            return False




print(Solution().backspaceCompare(S = "a##c", T = "#c"))