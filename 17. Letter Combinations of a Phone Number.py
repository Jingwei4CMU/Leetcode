class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        digits = list(digits)
        dic = {}
        dic['2'] = ['a','b','c']
        dic['3'] = ['d','e','f']
        dic['4'] = ['g','h','i']
        dic['5'] = ['j','k','l']
        dic['6'] = ['m','n','o']
        dic['7'] = ['p','q','r','s']
        dic['8'] = ['t','u','v']
        dic['9'] = ['w','x','y','z']
        result = ['']
        while digits:
            temp = digits.pop(0)
            new_result = []
            for prev in result:
                for to_add in dic[temp]:
                    new_result.append(prev+to_add)
            result = new_result
        return result

a = '23'
print(Solution().letterCombinations(a))