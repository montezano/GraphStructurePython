# -*- coding: utf-8 -*-
from GraphStructure import GraphStructure
import os



graph = GraphStructure()

path = "texts/"

# file = open('textoBom', 'r')
for filename in os.listdir(path):
    filename = path + filename
    file = open(filename, 'r')

    word = file.readline()
    word = word.rstrip('\n')
    graph.addVertice(word)
    
    for wordAuxBom in file:
        wordAuxBom = wordAuxBom.rstrip('\n')
        graph.addVertice(wordAuxBom)
        graph.connect(word, wordAuxBom)
        word = wordAuxBom

    print "Report of " + filename + ":"
    print "Average output degree: " + str(graph.averageDegree())
    print "Average clustering coefficient: " + str(graph.averageClusteringCoeffient())
    print "Averate shortest path: " + str(graph.averageShortestPath()) + "\n"
    graph.reset()

# print ""
# print ""
# print ""
# print ""
# print ""

# graphRuim = GraphStructure()

# file = open('textoRuim', 'r')

# wordRuim = file.readline()
# wordRuim = wordRuim.rstrip('\n')
# graphRuim.addVertice(wordRuim)

# for wordAuxRuim in file:
#     wordAuxRuim = wordAuxRuim.rstrip('\n')

#     graphRuim.addVertice(wordAuxRuim)
#     graphRuim.connect(wordRuim, wordAuxRuim)
#     wordRuim = wordAuxRuim
        
# graphRuim.printGraph()

# print "Report:\n"
# print "Average degree: " + str(graphRuim.averageDegree())

# graphRuim.neighborhoodOf("Maria")