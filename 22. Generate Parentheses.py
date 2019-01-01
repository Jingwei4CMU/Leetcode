import copy
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        bigstr = ''
        prev = []
        to_add = n
        result = []

        def genParen(prev, to_add, bigstr):
            print(prev,to_add,bigstr)
            if to_add == 0:
                for i in range(len(prev)):
                    bigstr += ')'
                result.append(bigstr)
                return
            if prev:
                # both option
                # do '('
                prev2 = copy.deepcopy(prev)
                bigstr2 = bigstr
                to_add2 = to_add

                prev.append('(')
                bigstr += '('
                to_add -= 1
                genParen(prev, to_add, bigstr)

                prev2.pop()
                bigstr2 += ')'
                to_add2 = to_add2
                genParen(prev2, to_add2, bigstr2)

            else:
                prev.append('(')
                bigstr += '('
                to_add -= 1
                genParen(prev, to_add, bigstr)

        genParen(prev, to_add, bigstr)
        return result


print(Solution().generateParenthesis(3))