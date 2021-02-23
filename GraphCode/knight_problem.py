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
            nodeId = posToNodeId(row,col,bdsize)
            # 单步合法走棋
            newPositions = genLegalMoves(row, col, bdsize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdsize)
                # 添加边和顶点
                ktGrapth.addEdge(nodeId, nid)
    return ktGrapth

def posToNodeId(row, col, bdsize):
    return row*bdsize + col


def knightTour(n, path, u, limit):
    """

    :param n: 层次
    :param path: 路径
    :param u: 当前顶点
    :param limit: 搜索总深度
    :return:
    目前实现的算法,其复杂度为O(k^n),其中n是棋盘格数目
    """
    u.setColor('gray')
    # 当前顶点加入路径
    path.append(u)
    if n < limit:
        # 对所有合法移动逐一深入
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            # 选择白色未经过的顶点深入
            if nbrList[i].getColor() == 'white':
                # 层次加1,递归深入
                done = knightTour(n+1, path, nbrList[i], limit)
            i = i+1
        if not done:
            # 都无法完成总深度,回溯,试本层下一个顶点
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done


















