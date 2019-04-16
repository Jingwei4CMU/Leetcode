class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        running = []
        dic = {}
        for log in logs:
            funid, s, time = log.split(':')
            funid = int(funid)
            time = int(time)
            if running == []:
                start = time
                running.append(funid)
            else:
                if s == 'start':
                    preruntime = time - start
                    if running[-1] in dic:
                        dic[running[-1]] += preruntime
                    else:
                        dic[running[-1]] = preruntime
                    running.append(funid)
                    start = time
                else:
                    runtime = time - start + 1
                    if funid in dic:
                        dic[funid] += runtime
                    else:
                        dic[funid] = runtime
                    running.pop()
                    start = time + 1
            res = []
        for i in range(n):
            res.append(dic[i])
        return res


n = 2
logs = ["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
print(Solution().exclusiveTime(n, logs))