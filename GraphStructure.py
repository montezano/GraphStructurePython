class GraphStructure(object):
        
    vertices = {}

    def __ini__(self):
        pass
    
    def addVertice(self, vertex):
        self.vertices[vertex] = {}
    
    def removeVertice(self, vertice):
        adjacents = self.vertices[vertice]
        for adjacent in adjacents:
            self.vertices[adjacent].remove(vertice)
        del self.vertices[vertice]
    
    def connect(self, vertice1, vertice2, value):
        self.vertices[vertice1].update({vertice2: value})
        self.vertices[vertice2].update({vertice1: value})
    
    def disconect(self, vertice1, vertice2):
        self.vertices[vertice1].remove(vertice2)
        self.vertices[vertice2].remove(vertice1)
        
    def order(self):
        return len(self.vertices)
        
    def getVertices(self):
        return self.vertices
    
    def getVertice(self):
        return self.vertices.keys()[0]
        
    def adjacentsOf(self, vertice):
        return self.vertices[vertice].keys()
    
    def degreeOf(self, vertice):
        return len(self.vertices[vertice])
        
    def isRegular(self):
        size = len(self.vertices.values()[0])
        for vertice in self.vertices:
            if not len(vertice.keys) == size:
                return False
        return True
        
    def isComplete(self):
        degree = len(self.vertices) - 1
        for vertice in self.vertices:
            if len(vertice.values()) != degree:
                return False
        return True
    
    def transitiveClosureOf(self, vertex):
        closure = []
        self.transitiveClosure(vertex, closure)
        return closure
        
        
    def transitiveClosure(self, vertex, vertexList):
        if vertex not in vertexList:
            vertexList.append(vertex)
            for adjacent in self.vertices[vertex].keys():
                self.transitiveClosure(adjacent, vertexList)
    
    def connected(self):
        if self.vertices:
            closure = self.transitiveClosureOf(self.vertices.keys()[0])
            for vertex in self.vertices:
                if vertex not in closure:
                    return False
            return True
        return False
        
    
    def findCicle(self):
        visited = []
        return self.connected() and not self.findCicleOf(self.vertices.keys()[0], self.vertices.keys()[0], visited)
        
    def findCicleOf(self, currentVertex, lastVertex, visited):
        if currentVertex in visited:
            return True
        visited.append(currentVertex)
        for adjacent in self.vertices[currentVertex]:
            if adjacent != lastVertex:
                if self.findCicleOf(adjacent, currentVertex, visited):
                    return True
        visited.remove(currentVertex)
        return False
    
    def shortestPath(self, initial, final):
        verticesList = self.vertices.keys()
        
        path_vertices = dict.fromkeys(self.vertices.keys(), initial)
        path_values = dict.fromkeys(self.vertices.keys(), 3654654564546)
        closure = initial
        current_length = 0
        next_closure = closure        
        while verticesList:
            shortest_value = 654687877463357456

            for aux_vertex in self.vertices[closure].keys():
                print "closure"
                print closure
                print "adjacent"
                print aux_vertex
                print "all_adjacents"
                print self.vertices[closure]
                closure_to_aux_vertex = current_length + self.vertices[closure][aux_vertex]
                if closure_to_aux_vertex < path_values[aux_vertex] and aux_vertex in verticesList:
                    path_values[aux_vertex] = closure_to_aux_vertex
                    path_vertices[aux_vertex] = closure
                    if shortest_value >= closure_to_aux_vertex:
                        shortest_value = closure_to_aux_vertex
                        next_closure = aux_vertex
                    
            verticesList.remove(closure)
            closure = next_closure
            current_length = path_values[closure]
            
                
        return path_vertices
        
    def printTest(self, aux_vertex):
        closure = self.vertices.keys()[0]
        print closure
        print self.vertices[closure][aux_vertex]
        
        # 20154117266958
        # 20150117268625
        # 20158117269943
        #BD: 3466645
graph = GraphStructure()
graph.addVertice('A')
graph.addVertice('B')
graph.addVertice('C')
graph.addVertice('D')
graph.addVertice('E')
#connect(3, 2)

graph.connect('A', 'B', 3)
graph.connect('B', 'C', 4)
graph.connect('B', 'E', 12)
graph.connect('C', 'D', 2)
graph.connect('D', 'E', 2)

# print graph.adjacentsOf('B')

# print graph.degreeOf('C')

# print graph.findCicle()

print graph.shortestPath('A', 'E')



