from EdmondKarp import *
from FordFulkerson import *

def minCut(commonRegion):
  
    source = 0; 
    sink = len(commonRegion) - 1 
    edmond_k= EdmondKarp(commonRegion) 
    left,right,visited = edmond_k.edmondKarp(source, sink)
    #ford_f = FordFulkerson(commonRegion)
    #visited = ford_f.fordFulkerson(source,sink)
    
    return left,right,visited

