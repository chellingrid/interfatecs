from collections import deque


# A queue node used in BFS
class Node:
	# (x, y) represents coordinates of a cell in the matrix
	# maintain a parent node for the printing path
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def __repr__(self):
        return str((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# Below lists detail all four possible movements from a cell
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]


# The function returns false if (x, y) is not a valid position
def isValid(x, y, l, c):
    return (0 <= x < l) and (0 <= y < c)


# Utility function to find path from source to destination
def getPath(node, path=[]):
    if node:
        getPath(node.parent, path)
        path.append(node)


# Find the shortest route in a matrix from source cell (x, y) to
# destination cell end
def findPath(matrix, start, end, lines, columns):	# `l × c` matrix
    x= start[0]
    y= start[1]

    # create a queue and enqueue the first node
    q = deque()
    src = Node(x, y)
    q.append(src)

    # set to check if the matrix cell is visited before or not
    visited = set()

    key = (src.x, src.y)
    visited.add(key)

    # loop till queue is empty
    while q:
        # dequeue front node and process it
        curr = q.popleft()
        i = curr.x
        j = curr.y

        # return if the destination is found
        if i == end[0] and j == end[1]:
            path = []
            getPath(curr, path)
            return path

        # value of the current cell
        n = matrix[i][j]

        # check all four possible movements from the current cell
        # and recur for each valid movement
        for k in range(len(row)):
            # get next position coordinates using the value of the current cell
            x = i + row[k]*n 
            y = j + col[k]*n

            # check if it is possible to go to the next position
            # from the current position
            if isValid(x, y, lines, columns):
                # construct the next cell node
                next = Node(x, y, curr)
                key = (next.x, next.y)

                # if it isn't visited yet
                if key not in visited:
                    # enqueue it and mark it as visited
                    q.append(next)
                    visited.add(key)

    # return None if the path is not possible
    return None



	

def busca1(g, orig, dest):
    if orig == dest: return 0
    if g[orig][dest] != 0: return g[orig][dest]
    for i in range(len(g[orig])):
        if g[orig][i] != 0:
            if busca1(g, i, dest): return g[i][dest]
    return False

def find_shortest_path(graph, start, end):
    dist = {start: start}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    return dist.get(end)

p = int(input()) #power
l,c = map(int,input().split(" ")) #dimensões do cenário
scenary = []

start = [0,0]
end = [0,0]
for i in range(l):
    values = list(input().split())
    for j in range(c):
        if values[j] == '.':
            values[j] = 1
        elif values[j] == '#':
            values[j] = 0
        elif values[j] == 'S':
            values[j] = 1
            start = [i,j]
        elif values[j] == 'K':
            values[j] = 1
            end = [i,j]
        else: #monstro
            if p >= int(values[j]):
                values[j] = 1
            else:
                values[j] = 0
    scenary.append(values)
find_shortest_path(scenary, start, end)
##path = findPath(scenary, start, end, l, c)
##
##if  path:
##    print(len(path)-1)
##else:
##    print('N') 
