class FordFulkerson:
    def __init__(self,commonRegion) -> None:
        self.visitedCount = 1
        self.commonRegion = commonRegion      
    def fordFulkerson(self,source,sink):
        x=len(self.commonRegion)
        visited=[0]*x
        visited_arr=[False]*x
        maximum_flow=0
        while(True):
            flow=self.depth(self.commonRegion,visited,source,sink,float('inf'))
            self.visitedCount += 1   
            maximum_flow+= flow
            if flow<=1e-4:
                for i in range(0,x):
                    if (visited[i]==self.visitedCount-1):
                         visited_arr[i]=True
                return visited_arr          
    def depth(self,commonRegion,visited,node,sink,flow):
        if (node==sink): 
            return flow
        next = commonRegion[node]
        visited[node] = self.visitedCount
        for i in range(len(next)):
            if visited[i] != self.visitedCount and next[i]>0:
                if (next[i]<flow):
                    flow =next[i]
                flow =self.depth(commonRegion,visited,i,sink,flow)
                if (flow>0.5):
                    commonRegion[node][i]=commonRegion[node][i]-flow
                    commonRegion[i][node]=commonRegion[i][node]+flow
                    return flow
        return 0

#REFERRED FROM GEEKS FOR GEEKS






