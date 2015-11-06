vertices = {}


def addVertice(vertice):
    adjacents = []
    vertices[vertice] = adjacents

def removeVertice(vertice):
    adjacents = vertices[vertice]
    for adjacent in adjacents:
        aux_list = vertices[adjacent]
        aux_list.remove(vertice)
    del vertices[vertice]

def connect(vertice1, vertice2):
    vertices[vertice1].append(vertice2)
    vertices[vertice2].append(vertice1)

def disconect(vertice1, vertice2):
    vertices[vertice1].remove(vertice2)
    vertices[vertice2].remove(vertice1)
    
def order():
    return len(vertices)
    
def getVertices():
    return vertices

def getVertice():
    return vertices.keys()[0]
    
def adjacentsOf(vertice):
    return vertices[vertice]

def degreeOf(vertice):
    return len(vertices[vertice])
    
def isRegular():
    size = len(vertices.values()[0])
    for vertice in vertices:
        if not len(vertice.keys) == size:
            return False
    return True
    
def isComplete():
    degree = len(vertices) - 1
    for vertice in vertices:
        if len(vertice.values()) != degree:
            return False
    return True

def transitiveClosureOf(vertex):
    closure = []
    transitiveClosure(vertex, closure)
    return closure
    
    
def transitiveClosure(vertex, vertexList):
    if vertex not in vertexList:
        vertexList.append(vertex)
        for adjacent in vertices[vertex]:
            transitiveClosure(adjacent, vertexList)

def connected():
    if vertices:
        closure = transitiveClosureOf(vertices.keys()[0])
        for vertex in vertices:
            if vertex not in closure:
                return False
        return True
    return False
    

def findCicle():
    visited = []
    return connected() and not findCicleOf(vertices.keys()[0], vertices.keys()[0], visited)
    
def findCicleOf(currentVertex, lastVertex, visited):
    if currentVertex in visited:
        return True
    visited.append(currentVertex)
    for adjacent in vertices[currentVertex]:
        if adjacent != lastVertex:
            if findCicleOf(adjacent, currentVertex, visited):
                return True
    visited.remove(currentVertex)
    return False
    
addVertice(1)
addVertice(2)
addVertice(3)
addVertice(4)
#connect(3, 2)

connect(1, 2)
connect(1, 3)

for adjacent in adjacentsOf(1):
    print adjacent

print transitiveClosureOf(1)


print degreeOf(1)

print findCicle()

