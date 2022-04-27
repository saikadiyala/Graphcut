from audioop import avg
import numpy as np
import os
import json
COUNT=0
def calculateAvg(array):
    total = 0
    for i in array:
        total+=i
    
    return total/len(array)

def graphConstruction(patch1, patch2):
    global COUNT
    nodes = patch1.shape[0] * patch1.shape[1] + 2    
    graph = [[0]*(nodes) for row in range(nodes)]
    map2Original = {}
    count = 1
    for r in range(len(patch1[0])):
        for c in range(len(patch1)):
            map2Original[count] = (c,r)
            count += 1
    count -= 1
    for r in range(0,nodes):
        for c in range(0,nodes):
            if (r == 0 and 1<=c<=len(patch1)) or (c == nodes-1 and count-len(patch1)<=r<=count):
                graph[r][c] = float('inf')

    calculateAvg(patch1[0][2])
    for i in range(1,len(patch1)):
        for j in range(0,len(patch1[0])):

            if(j+1< len(patch1[0])):

                graph[i][j] = abs(calculateAvg(patch1[i-1][j]) - calculateAvg(patch2[i][j])) #+ calculateAvg(abs(patch1[i-1][j+1] - patch2[i-1][j+1])) + 1
            
                graph[i][j] = abs(calculateAvg(patch1[i-1][j]) - calculateAvg(patch2[i-1][j])) #+ abs(calculateAvg(patch1[i][j]) - calculateAvg(patch2[i-1][j])) +1
            

    
    dirt = os.getcwd()
    with open(os.path.join(dirt, "Adj_matrice_file" + str(COUNT)+ ".txt"), 'w') as new_file:
        json.dump(graph, new_file)
        COUNT=COUNT+1
    return graph  
  

    




