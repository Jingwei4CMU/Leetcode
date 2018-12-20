class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return 1
        temp = None
        p1 = 0
        count = 0
        addlist = []
        for i in range(len(chars)):
            if not temp:
                temp = chars[i]
                count = 1
                addlist.append(chars[i])
            elif chars[i] == temp:
                count += 1
            else:
                temp = chars[i]
                addlist.append(str(count))
                addlist.append(chars[i])
                count = 1
            while (len(addlist) > 0) and p1 <= i:
                chars[p1] = addlist.pop(0)
                p1 += 1
        addlist.append(str(count))
        # print(addlist)
        while len(addlist) > 0 and p1 < len(chars):
            chars[p1] = addlist.pop(0)
            p1 += 1
        # print(chars)
        return p1







a = ["a","a","b","b","c","c","c"]
print(Solution().compress(a))