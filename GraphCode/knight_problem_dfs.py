# coding: utf-8
# from . import graph_ccc
from GraphCode.graph_ccc import *


def genLegalMoves(x, y, bdsize):
    newMoves = []
    # 马走日8个格子
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdsize) and legalCoord(newY, bdsize):
            newMoves.append((newX, newY))
    return newMoves


# 确认不会走出棋盘
def legalCoord(x, bdsize):
    if 0 <= x < bdsize:
        return True
    else:
        return False


# 构建走棋关系图
def knightGraph(bdsize):
    ktGrapth = Graph()
    # 遍历每个格子
    for row in range(bdsize):
        for col in range(bdsize):
            nodeId = posToNodeId(row, col, bdsize)
            # 单步合法走棋
            newPositions = genLegalMoves(row, col, bdsize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdsize)
                # 添加边和顶点
                ktGrapth.addEdge(nodeId, nid)
    return ktGrapth


def posToNodeId(row, col, bdsize):
    """
    将坐标转化为id, row
    row和col都是从0开始的
    pos:  (0,0)(0,1)(0,2)(0,3),(0,4)
    id:    0     1     2    3     4
    :param row:
    :param col:
    :param bdsize:
    :return:
    """
    return row * bdsize + col

def orderbyAvail(n):
    resultList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c += 1
            resultList.append((c,v))
    resultList.sort(key=lambda x:x[0])
    return [y[1] for y in resultList]

def knightTour(n, path, u, limit):
    """
    knightTour(0, [], 4, 63)
    :param n: 层次, 是搜索树的当前深度
    :param path: 路径, 是到目前为止访问到的顶点列表
    :param u: 当前顶点, 是希望在图中访问的顶点
    :param limit: 搜索总深度, 路径上的顶点总数
    :return:
    目前实现的算法,其复杂度为O(k^n),其中n是棋盘格数目
    """
    u.setColor('gray')
    # 当前顶点加入路径
    path.append(u)
    if n < limit:
        # 对所有合法移动逐一深入
        # nbrList = list(u.getConnections())
        nbrList = list(orderbyAvail(u))
        i = 0
        done = False
        while i < len(nbrList) and not done:
            # 选择白色未经过的顶点深入
            if nbrList[i].getColor() == 'white':
                # 层次加1,递归深入
                done = knightTour(n + 1, path, nbrList[i], limit)
            i = i + 1
        if not done:
            # 都无法完成总深度,回溯,试本层下一个顶点
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done


if __name__ == '__main__':
    g = knightGraph(8)
    # for i in g:
    #     print(i)

    path = []
    startVertex = g.getVertex(4)
    knightTour(0, path, startVertex, 63)
    # print(path)
    for node in path:
        print(node.getId(), end=" ")
