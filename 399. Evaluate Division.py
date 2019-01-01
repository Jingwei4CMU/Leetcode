class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dic = {}
        for i in range(len(equations)):
            if equations[i][0] in dic:
                dic[equations[i][0]].append((equations[i][1], values[i]))
            else:
                dic[equations[i][0]] = [(equations[i][1], values[i])]
            if values[i] != 0:
                tempvalue = 1 / values[i]
                if equations[i][1] in dic:
                    dic[equations[i][1]].append((equations[i][0], tempvalue))
                else:
                    dic[equations[i][1]] = [(equations[i][0], tempvalue)]
        allresult = []

        def getproduct(query):
            searchedset = set()
            searchlist = [(query[0], 1)]
            while searchlist:
                nowstr, nowval = searchlist.pop(0)
                if nowstr == query[1]:
                    if query[i] in dic:
                        return nowval
                    else:
                        return -1
                if nowstr in searchedset:
                    continue
                searchedset.add(nowstr)
                if nowstr in dic:
                    to_search = dic[nowstr]
                    for toto in to_search:
                        toto = (toto[0], toto[i] * nowval)
                        searchlist.append(toto)

            return -1

        for query in queries:
            allresult.append(getproduct(query))
            print(allresult)
        return allresult

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print(Solution().calcEquation(equations, values, queries))


