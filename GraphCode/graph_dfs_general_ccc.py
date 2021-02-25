# coding: utf-8

from pythonds.graphs import Graph
# 通用深度优先搜索

# class DFSGraph(Graph):
#     def __init__(self):
#         super().__init__()
#
#     def dfs(self):
#         for v in self:
#             v.setColor("white")
#             v.setPred(None)
#
#         for v in self:
#             self.dfsvisit(v)
#
#     def dfsvisit(self, startV):
#         startV.setColor("gray")
#
#         for nbr in startV.getConnections():
#             if nbr.getColor() == "white":
#                 nbr.setPred(startV)
#                 self.dfsvisit(nbr)
#         startV.setColor('black')
#         print(startV.getId(), end=" ")

class DFSGraph(Graph):
    """
    time, 发现时间,结束时间对于深度遍历是没有用的
    主要是用于强连通和拓扑
    """
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        # 颜色的初始化, 将所有顶点的颜色都置为白色,前驱都为-1
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            # 如果还有未包括的顶点,则建森林
            if aVertex.getColor() == 'white':
                print("wwwwwwwwww",aVertex.getId())
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):

        startVertex.setColor('gray')
        # 算法的步数加一
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                # 深度优先递归访问
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)
        print(startVertex.getId(), end=" ")


if __name__ == '__main__':

    g = DFSGraph()
    for i in range(6):
        g.addVertex(i)
    # print(g.vertList)
    g.addEdge(0, 1, 5)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)

    g.addEdge(4, 0, 1)
    g.addEdge(0, 5, 2)
    g.addEdge(5, 4, 8)
    g.addEdge(3, 5, 3)
    g.addEdge(5, 2, 1)
    g.dfs()

    # g = DFSGraph()
    # g.addVertex('A')
    # g.addVertex('B')
    # g.addVertex('C')
    # g.addVertex('D')
    # g.addVertex('E')
    # g.addVertex('F')
    # g.addEdge('A', 'B', 1)
    # g.addEdge('B', 'C', 1)
    # g.addEdge('A', 'D', 1)
    # g.addEdge('B', 'D', 1)
    # g.addEdge('D', 'E', 1)
    # g.addEdge('E', 'F', 1)
    # g.addEdge('F', 'C', 1)
    # g.addEdge('E', 'B', 1)
    # g.dfs()