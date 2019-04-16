class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def dp(part):
            if '[' in part:
                index = 0
                while ord(part[index]) >= 65:
                    index += 1
                pre = part[:index]
                num = 0
                while ord(part[index]) <= 57:
                    num *= 10
                    num += ord(part[index])-48
                    index += 1
                paran = 1
                index += 1
                startindex = index
                while paran > 0:
                    if part[index] == '[':
                        paran += 1
                    elif part[index] == ']':
                        paran -= 1
                    index += 1
                to_return = dp(part[startindex:index-1])*num
                if index == len(part):
                    return pre + to_return
                else:
                    return pre + to_return + dp(part[index:])
            else:
                return part
        return dp(s)

s = "3[a2[c]]"
print(Solution().decodeString(s))