class EdmondKarp: 
    def __init__(self,commonRegion): 
        self.commonRegion=commonRegion.copy()
        self.row=len(commonRegion) 
        self.col = len(commonRegion[0])
        self.organ_graph=[i[:] for i in commonRegion]
    def edmondKarp(self,source,sink): 
        pix=[]
        global COUNT
        maximumFlow=0
        temporarySource=0
        parent = [-1]*(self.row) 
        while self.breadth(source, sink, parent) : 
            flow = float("Inf") 
            temporarySource = sink 
            while(temporarySource!=source): 
                flow = min (flow, self.commonRegion[parent[temporarySource]][temporarySource]) 
                temporarySource = parent[temporarySource] 
            maximumFlow=maximumFlow+flow 
            temp_sink = sink
            while(temp_sink != source): 
                temporarySource = parent[temp_sink] 
                self.commonRegion[temporarySource][temp_sink]=self.commonRegion[temporarySource][temp_sink]-flow 
                self.commonRegion[temp_sink][temporarySource]=self.commonRegion[temp_sink][temporarySource]+flow 
                temp_sink = parent[temp_sink] 
        visited=len(self.commonRegion)*[False]
        self.depth(self.commonRegion,temporarySource,visited)

        left=[]
        right=[]
        for i  in range(0,self.row):
            for j in range(0,self.col):
                if self.commonRegion[i][j] == 0 and self.organ_graph[i][j]>0 and visited[i]:
                    left.append(i)
                    right.append(j)               
                    pix.append(str(i)+"-"+str(j))
     
                    
                                   
        return left,right,visited
    def breadth(self,source, target, parent): 
        visited =[False]*(self.row) 
        queue=[] 
        queue.append(source) 
        visited[source] = True
        while queue:
            node = queue.pop(0) 
            for i, val in enumerate(self.commonRegion[node]): 
                if visited[i]==False and val>0 : 
                    queue.append(i) 
                    visited[i]=True
                    parent[i]=node 
        return True if visited[target] else False
         
    def depth(self, commonRegion,source,visited):
        visited[source]=True
        for i in range(len(commonRegion)):
            if commonRegion[source][i]>0 and not visited[i]:
                self.depth(commonRegion,i,visited)
                
  #REFERRED FROM GEEKS FOR GEEKS