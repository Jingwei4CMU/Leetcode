# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        copydic = {}
        res = UndirectedGraphNode(node.label)
        newdic = {res.label: res}
        mapdic = {res:node}
        todo = [res]
        while todo:
            temp = todo.pop(0)
            if temp in copydic:
                continue
            for i in mapdic[temp].neighbors:
                if i.label in newdic:
                    temp.neighbors.append(newdic[i.label])
                else:
                    toadd = UndirectedGraphNode(i.label)
                    temp.neighbors.append(toadd)
                    todo.append(toadd)
            newdic[temp.label] = temp
            copydic[temp] = 1
        return res

node = UndirectedGraphNode(0)
node.neighbors = [node,node]
res = Solution().cloneGraph(node)

print(res)
print(res.neighbors)