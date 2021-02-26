# coding: utf-8

# from pythonds.graphs import Graph
import graph_ccc


# 通用深度优先搜索
class DFSGraph(graph_ccc.Graph):
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
                # print("wwwwwwwwww",aVertex.getId())
                self.dfsvisit(aVertex)

    def dfsEx(self):
        # 颜色的初始化, 将所有顶点的颜色都置为白色,前驱都为-1
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        lst = list(self.vertList.values())
        lst.sort(key=lambda v: -v.fin)
        mydict = {}
        for v in lst:
            # 如果还有未包括的顶点,则建森林
            if v.getColor() == 'white':
                # print("wwwwwwwwww",aVertex.getId())
                mydict[v.getId()] = []
                self.dfsvisitEx(v, mydict[v.getId()])
        return mydict

    def dfsvisitEx(self, startVertex, path):
        path.append(startVertex)
        startVertex.setColor('gray')
        # 算法的步数加一
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                # 深度优先递归访问
                self.dfsvisitEx(nextVertex, path)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)
        print(startVertex.getId(), end=" ")

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
    # g.addVertex('A')
    # g.addVertex('B')
    # g.addVertex('C')
    # g.addVertex('D')
    # g.addVertex('E')
    # g.addVertex('F')
    # g.addVertex('G')
    # g.addVertex('H')
    # g.addVertex('I')
    g.addEdge('A', 'B')
    g.addEdge('B', 'E')
    g.addEdge('E', 'D')
    g.addEdge('D', 'B')
    g.addEdge('E', 'A')
    g.addEdge('D', 'G')
    g.addEdge('G', 'E')
    g.addEdge('B', 'C')
    g.addEdge('C', 'F')
    g.addEdge('F', 'H')
    g.addEdge('H', 'I')
    g.addEdge('I', 'F')

    # 1. 对图调用DFS算法,为每个顶点计算"结束时间"
    g.dfs()
    print("\n")
    for node in g:
        print(node, node.disc, node.fin)

    # 2.对图进行转置操作
    gt = DFSGraph()
    for node in g:
        for nbr in node.connectedTo.keys():
            gt.addEdge(nbr.getId(), node.getId())
            # 保留以前遍历出来的开始时间和结束时间
            start = gt.getVertex(nbr.getId())
            start.disc = nbr.disc
            start.fin = nbr.fin

            end = gt.getVertex(node.getId())
            end.disc = node.disc
            end.fin = node.fin

    #     print(node.getId(), node.getFinish(), node.getDiscovery())
    print("=" * 30)

    for node in gt:
        print(node, node.disc, node.fin)
    # 3.对转置图调用dfs算法,对每个顶点的搜索循环里,要以顶点"结束时间倒序的顺序来搜索
    mydict = gt.dfsEx()
    print("=" * 70)
    # print(mydict)
    # 4. 最后,深度优先森林中的每一棵树都是一个强连通分支
    """
    A,E,B,D,G,
    C,
    F,I,H,
    """
    for item in mydict.items():
        for node in item[1]:
            print(node.getId(), end=",")
        print()