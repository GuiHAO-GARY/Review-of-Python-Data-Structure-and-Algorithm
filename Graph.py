import operator
from Basic_Data_Structure import Queue
from Tree import PriorityQueue
import sys


# Define vertex and graph class
class Vertex:
    def __init__(self, key):
        self.id = key  # name of the vertex
        self.connectedTo = {}  # connection towards other vertices
        self.distance = None
        self.predecessor = None
        self.color = 'white'
        self.discoveryTime = None
        self.finishTime = None

    def addNeighbor(self, nbr, weight=0):
        """
        :param nbr: neighbor vertex instance to be connected: this vertex ---> nbr
        :param weight: weight of connection
        :return: None, but add edge between this vertex and nbr
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        """
        :return: print 'Certain vertex connectedTo A vertex, B vertex, ...
        """
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """
        :return: all neighborhood vertex object
        """
        return self.connectedTo.keys()

    def getId(self):
        """
        :return: Name of this vertex
        """
        return self.id

    def getWeight(self, nbr):
        """
        :param nbr: Another neighbor vertex
        :return: the weight of this connection
        """
        if nbr in self.getConnections():
            return self.connectedTo[nbr]
        else:
            return None

    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setPred(self, predecessor):
        self.predecessor = predecessor

    def getPred(self):
        return self.predecessor

    def setDiscovery(self, time):
        self.discoveryTime = time

    def setFinish(self, time):
        self.finishTime = time


class Graph:
    def __init__(self):
        self.vertList = {}  # Store the vertices in this graph
        self.numVertices = 0  # number of vertices in this graph

    def addVertex(self, key):
        self.numVertices += 1  # add number once adding one vertex into this graph
        newVertex = Vertex(key)  # Create a new vertex
        self.vertList[key] = newVertex  # Store new vertex into graph instance, the name is the same as name of vertex

    def getVertex(self, key):
        """
        :param key: name of vertex
        :return: vertex called 'key' or None when there is no such a vertex called 'key'
        """
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self, fkey, tkey, cost=0):
        """
        :param fkey: from vertex key
        :param tkey: to vertex key
        :param cost: weight
        :return: None. Just add edge between two vertices
        """
        if fkey not in self.vertList:  # if from vertex has not been created yet, first create it
            self.addVertex(fkey)
        if tkey not in self.vertList:  # if to vertex has not been created yet, first create it
            self.addVertex(tkey)
        self.vertList[fkey].addNeighbor(self.vertList[tkey], weight=cost)  # Using method addNeighbor
        # in Vertex class to link two vertex

    def getVertices(self):  # Traverse all names of vertices in graph
        return self.vertList.keys()

    def __iter__(self):  # Traverse all vertices in graph
        return iter(self.vertList.values())


g = Graph()
for i in range(6):
    g.addVertex(i)
g.vertList
g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)

for v in g:  # __iter__ method defines v is every vertex in graph
    for w in v.getConnections():
        print('(%s, %s)' % (v.getId(), w.getId()))


# Try
Vertex_try = g.vertList[5]
Vertex_try.getId()
str(Vertex_try)
Vertex_try.getConnections()
Vertex_try.getWeight(g.vertList[4])
1 in g
g.numVertices
g.getVertex(2)  # equals to g.vertList[2]
g.getVertices()  # return keys (or names) of vertices


# 1. Word ladder
def buildGraph(wordFile):
    d = {}  # Create a dictionary to store the bucket
    g = Graph()  # Create a graph instance
    wfile = open(wordFile, 'r')  # Open word file
    # Create word bucket
    for line in wfile:
        word = line[:-1]  # this is one word in one line
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]  # bucket key
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


# 2. Breadth first search
def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()  # Create a queue
    vertQueue.enqueue(start)  # add start vertex into queue
    while vertQueue.size() > 0:  # if queue has at least one vertex
        currentVert = vertQueue.dequeue()  # current vertex is the element at head of queue (first in)
        for nbr in currentVert.getConnections():  # current vertex's neighbor vertices
            if nbr.getColor() == 'white':  # if this color is white: has never been visited
                nbr.setColor('gray')  # set color as gray to show it has been visited at least one time,
                # but there are other vertices have access to it and has not visited yet.
                nbr.setDistance(currentVert.getDistance() + 1)  # distance from the start
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)  # add this nbr in queue
        currentVert.setColor('black')  # no other vertices have access to currentVert since this a non directional graph
        # this makes other vertices won't visit this currentVert any more


def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())


# try
g = buildGraph('words.txt')
bfs(g, start=g.getVertex('fool'))
traverse(g.getVertex('sage'))

g.getVertex('fool').getDistance()
g.getVertex('pool').getDistance()
g.getVertex('poll').getDistance()
g.getVertex('pole').getDistance()
g.getVertex('pale').getDistance()
g.getVertex('page').getDistance()
g.getVertex('sage').getDistance()
g.getVertex('sage').getPred().getId()


# E4
def shortestPath(g, start):
    bfs(g, start)
    for vertex in g:
        idList = []
        x = vertex
        num_count = 0
        while x.getPred():
            idList.append(x.getId())
            x = x.getPred()
            num_count += 1
        idList.append(start.getId())
        idList.reverse()
        print('{} Steps. Path:'.format(num_count) + '-->'.join(idList))


shortestPath(g, g.getVertex('fool'))

# E6
g = Graph()
g.addEdge('0', '3')
g.addEdge('3', '2')
g.addEdge('1', '4')
g.addEdge('2', '1')
g.addEdge('4', '0')

shortestPath(g, start=g.getVertex('0'))


# E7
def waterLoading(a_vol, b_vol, r_vol):
    g = Graph()
    start_vol = 0
    stop = False
    while not stop:
        if start_vol + b_vol < a_vol:
            g.addEdge(str(start_vol), str(start_vol + b_vol))
            start_vol += b_vol
        elif start_vol + b_vol > a_vol:
            g.addEdge(str(start_vol), str(start_vol + b_vol - a_vol))
            start_vol = start_vol + b_vol - a_vol
        else:
            g.addEdge(str(start_vol), str(a_vol))
            g.addEdge(str(a_vol), '0')
            stop = True

    bfs(g, start=g.getVertex('0'))
    idList = []
    if str(r_vol) in g:
        x = g.getVertex(str(r_vol))
        num_count = 0
        while x.getPred():
            idList.append(x.getId())
            x = x.getPred()
            num_count += 1
        idList.append('0')
        idList.reverse()
        print('{} Steps. Path:'.format(num_count) + '-->'.join(idList))
    else:
        print('Mission impossible')


waterLoading(10, 7, 3)


# 3. Knight Travelling
def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)  # Undefined yet
            newPositions = genLegalMoves(row, col, bdSize)  # Undefined yet
            for e in newPositions:
                nid = posToNodeId(e[0], e[1])
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def posToNodeId(row, col, bdSize):
    return row * bdSize + col


def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdSize):
    if 0 <= x < bdSize:
        return True
    else:
        False


def knightTour(n, path, u, limit):
    """
    :param n: Current depth of tree
    :param path: Visited vertices
    :param u: Target vertex
    :param limit: Total number of vertices
    :return: True or False to show whether we find 64 vertices in a path
    """
    u.setColor('gray')  # Visit current vertex and turn it from white to gray
    path.append(u)  # Add current vertex into path
    if n < limit:  # when current depth smaller than total number of vertices which means knight has not visited all v.
        nbrList = list(u.getConnections())  # List containing all connected vertices
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor == 'white':  # if this connection has not been visited
                done = knightTour(n+1, path, nbrList[i], limit)  # invoke knightTour in recursive way. if it returns
                # True it means from current vertex u and its connection nbrList[i] we find a path to visit all points
                # if it returns False it means from current vertex u and its connection nbrList[i] we cannot find a path
            i += 1
        if not done:  # This means all connections are impossible to find a final path
            path.pop()  # Then this vertex u is not suitable. We wipe it out of path
            u.setColor('white')  # Set its status as white
    else:  # when n = limits which means we have visited all points on the plate.
        done = True  # We find this path
    return done


def orderByAvail(n):
    # it can replace above u.getConnections() to order its connections (with least legal moves at the front/ at edge)
    # In this way we can get higher chance to end the loop and thus find the path more quickly
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c += 1
                resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


# 4. Depth first search graph
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')  # Set vertices in graph to white
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

    def transpose(self):
        newGraph = DFSGraph()
        for aVertex in self:
            for nbr in aVertex.getConnections():
                newGraph.addEdge(nbr.getId(), aVertex.getId())
        return newGraph

    def topologicalSort(self):
        self.dfs()
        topoList = [v for v in self]
        topoList.sort(key=operator.attrgetter('finishTime'), reverse=True)
        return topoList

    def IntensiveConnectedUnits(self):
        topoList = self.topologicalSort()
        nameList = [v.getId() for v in topoList]
        g_transpose = self.transpose()
        orderList = [g_transpose.getVertex(i) for i in nameList]
        for aVertex in g_transpose:
            aVertex.setColor('white')  # Set vertices in graph to white
            aVertex.setPred(-1)
        for aVertex in orderList:
            if aVertex.getColor() == 'white':
                g_transpose.dfsvisit(aVertex)
        topoList = [v for v in g_transpose]
        topoList.sort(key=operator.attrgetter('finishTime'), reverse=True)
        result = []
        temp = []
        for v in topoList:
            if v.getPred() == -1:
                result.append(temp)
                temp = [v]
            else:
                temp.append(v)
        result.append(temp)
        result.pop(0)
        for i in result:
            print([j.getId() for j in i])


# Try
g = DFSGraph()
g.addEdge('3/4 杯牛奶', '一杯松饼粉')
g.addEdge('一个鸡蛋', '一杯松饼粉')
g.addEdge('一勺油', '一杯松饼粉')
g.addEdge('一杯松饼粉', '倒入1/4杯')
g.addEdge('一杯松饼粉', '加热枫糖浆')
g.addEdge('加热平底锅', '倒入1/4杯')
g.addEdge('倒入1/4杯', '出现气泡时翻面')
g.addEdge('出现气泡时翻面', '开始享用')
g.addEdge('加热枫糖浆', '开始享用')
topoList = g.topologicalSort()
for v in topoList:
    print(v.getId())

# Try
g = DFSGraph()
g.addEdge('A', 'B')
g.addEdge('B', 'C')
g.addEdge('B', 'E')
g.addEdge('C', 'F')
g.addEdge('D', 'G')
g.addEdge('E', 'A')
g.addEdge('E', 'D')
g.addEdge('F', 'H')
g.addEdge('G', 'E')
g.addEdge('H', 'I')
g.addEdge('I', 'F')
#  g.dfs()

g.IntensiveConnectedUnits()


# 5. Dijkstra theory
def dijkstra(aGraph, start):
    pq = PriorityQueue()  # Create a priority queue
    start.setDistance(0)  # set start vertex distance as 0
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])  # build queue using key-value pairs, least distance is at the
    # head of queue
    while not pq.isEmpty():
        currentVert = pq.delMin()  # the smallest distance vertex
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)  # keep it as smallest distance
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)  # if a vertex distance decrease and it has been in queue, put them to
                # head of queue


# 6. Prim algorithm
def prim(G, start):
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newCost = currentVert.getWeight(nextVert) + currentVert.getDistance()
            if v in pq and newCost < nextVert.getDistance():
                nextVert.setPred(currentVert)
                nextVert.setDistance(newCost)
                pq.decreaseKey(nextVert, newCost)