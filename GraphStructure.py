# -*- coding: utf-8 -*-
#coding: utf-8
class GraphStructure(object):
        
    vertices = {}

    def __ini__(self):
        pass
    
    def reset(self):
        self.vertices = {}
    
    def addVertice(self, vertex):
        if vertex not in self.vertices.keys():
            self.vertices[vertex] = {}
    
    def removeVertice(self, vertice):
        adjacents = self.vertices[vertice]
        for adjacent in adjacents:
            self.vertices[adjacent].remove(vertice)
        del self.vertices[vertice]
    
    def connect(self, vertice1, vertice2):
        if vertice2 in self.adjacentsOf(vertice1):
            self.vertices[vertice1][vertice2] += 1
        else:
            self.vertices[vertice1].update({vertice2: 1})

        
#        self.vertices[vertice1].update({vertice2: value})
#        self.vertices[vertice2].update({vertice1: value})
            
    
    def disconect(self, vertice1, vertice2):
        self.vertices[vertice1].remove(vertice2)
        self.vertices[vertice2].remove(vertice1)
        
    def order(self):
        return len(self.vertices)
        
    def getVertices(self):
        return self.vertices.keys()
    
    def getVertice(self):
        return self.vertices.keys()[0]
        
    def adjacentOf(self, adjacent, of):
        return self in self.adjacentsOf(of)
        
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
    
    def shortestPath(self, initial, final, reachable):
        verticesList = []
        
        path_vertices = dict.fromkeys(self.vertices.keys(), initial)
        path_values = dict.fromkeys(self.vertices.keys(), 3654654564546)
        closure = initial
        current_length = 0
        next_closure = closure        
        for reach in reachable:
            shortest_value = 654687877463357456

            for aux_vertex in self.vertices[closure].keys():
                # print "closure"
                # print closure
                # print "adjacent"
                # print aux_vertex
                # print "all_adjacents"
                # print self.vertices[closure]
                closure_to_aux_vertex = current_length + self.vertices[closure][aux_vertex]
                if aux_vertex not in verticesList:
                    if closure_to_aux_vertex < path_values[aux_vertex]:
                            
                        path_values[aux_vertex] = closure_to_aux_vertex
                        path_vertices[aux_vertex] = closure
                        if shortest_value >= closure_to_aux_vertex:
                            shortest_value = closure_to_aux_vertex
                            next_closure = aux_vertex
                    else:
                        if path_values[aux_vertex] < closure_to_aux_vertex:
                            if shortest_value >= closure_to_aux_vertex:
                                shortest_value = closure_to_aux_vertex
                                next_closure = aux_vertex
                    
            verticesList.append(closure)
            closure = next_closure
            current_length = path_values[closure]
            
        aux_order = final
        shortest_path = []
        shortest_path.append(final)
        while aux_order != initial:
            aux_order = path_vertices[aux_order]
            shortest_path.append(aux_order)
            
        shortest_path.reverse()
        return shortest_path
        
    def printTest(self, aux_vertex):
        closure = self.vertices.keys()[0]
        print closure
        print self.vertices[closure][aux_vertex]
        
    def printGraph(self):
        for vertex in self.vertices:
            print "{0} adjacents: {1}".format(vertex, self.vertices[vertex])
    
    def averageDegree(self):
        degreeSum = 0.0;
        
        for vertex in self.vertices.values():
            degreeSum += sum(vertex.values())
        degreeSum = degreeSum / len(self.vertices)
        return degreeSum
            
            
    
    def neighborhoodOf(self, vertex):
        neighborhood = self.adjacentsOf(vertex)
        
        for vertexIt in self.vertices:
            
            if vertexIt != vertex:
                if vertexIt not in neighborhood:
                    if vertex in self.adjacentsOf(vertexIt):
                        neighborhood.append(vertexIt)
        return neighborhood
        
            
            
    def clusteringCoeffientOf(self, vertex):
        clusterCoefficient = 0.0
        neighborhood = self.neighborhoodOf(vertex)
        # print "neighbors of " + vertex + ":"
        # print neighborhood

        for neighbor in neighborhood:
            # print "neighbor: " + neighbor + " adjacents: "
            # print  self.adjacentsOf(neighbor)
            for neighborAdjacents in neighborhood:
                
                if neighborAdjacents in self.adjacentsOf(neighbor):
                    # print "bingo"
                    clusterCoefficient += 1

        if (len(neighborhood)*(len(neighborhood) - 1)) != 0:
            clusterCoefficient = clusterCoefficient / (len(neighborhood)*(len(neighborhood) - 1))
        # print vertex
        # print neighborhood
        # print (len(neighborhood)*(len(neighborhood) - 1))
        # print clusterCoefficient
        return clusterCoefficient
            
    def averageClusteringCoeffient(self):
        total = 0.0
        for vertex in self.getVertices():
            total += self.clusteringCoeffientOf(vertex)
        total = total / len(self.getVertices())
        return total
        
    def bfs(self, start):
        graph = self.getVertices()
        graph = set(graph)
        visited, queue = set(), [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(graph - visited)
        return visited
                
            
    def averageShortestPathOf(self, vertex):
        reachable = self.transitiveClosureOf(vertex)
        lenght = 0.0
        for reach in reachable:
            lenght += len(self.shortestPath(vertex, reach, reachable)) - 1.0

        lenght = lenght / len(reachable)
        return lenght
    
    def averageShortestPath(self):
        total = 0.0
        
        for vertex in self.getVertices():
            total += self.averageShortestPathOf(vertex)
        
        total = total / len(self.getVertices())
        return total

#graph = GraphStructure()
#graph.addVertice('A')
#graph.addVertice('B')
#graph.addVertice('C')
#graph.addVertice('D')
#graph.addVertice('E')
#connect(3, 2)

#graph.connect('A', 'B', 3)
#graph.connect('B', 'C', 4)
#graph.connect('B', 'E', 6)
#graph.connect('C', 'D', 2)
#graph.connect('D', 'E', 2)
#graph.connect('A', 'E', 5)

# print graph.adjacentsOf('B')

# print graph.degreeOf('C')

# print graph.findCicle()

#print graph.shortestPath('A', 'E')