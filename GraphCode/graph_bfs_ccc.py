# coding: utf-8
# from queue import Queue
# from pythonds.graphs import Graph, Vertex
import queue_orderdlist_ccc
import graph_ccc


def traverse(y):
    x = y
    # 当前驱不为None
    while x.getPred() != None:
        # 打印当前节点的id,就是这个单词
        print(x.getId())
        x = x.getPred()
    print(x.getId())


def buildGraph(wordFile):
    d = {}
    g = graph_ccc.Graph()
    wfile = open(wordFile, 'r')
    # 采用字典建立桶
    for line in wfile:
        word = line[:-1]
        # print("word++",word)
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            # print("bbbb", bucket)
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = queue_orderdlist_ccc.Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            # 说明还没有访问过
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


if __name__ == '__main__':
    # g = buildGraph('fourletterwords.txt')
    # for item in g.vertList.values():
    #     print(item)
    wordgraph = buildGraph("fourletterwords.txt")
    bfs(wordgraph, wordgraph.getVertex('FOOL'))
    traverse(wordgraph.getVertex('SAGE'))
