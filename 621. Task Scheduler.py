from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = Counter(tasks)
        res = 0
        if n == 0:
            return len(tasks)
        while counter:
            clen = len(counter)
            if n + 1 > clen:
                # should finish here and return
                most = counter.most_common(1)[0][1]
                res += (n + 1) * (most - 1)
                temp = counter.most_common(n + 1)
                for i, nn in temp:
                    if nn == most:
                        res += 1
                    else:
                        return res
                return res
            else:
                res += n+1
                temp = counter.most_common(n + 1)
                for i, nn in temp:
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]
        return res

a = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(Solution().leastInterval(a,n))