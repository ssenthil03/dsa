from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdges(self,u,v):
        self.graph[u].append(v)
    
    def BFT(self, s):
        
        visited = [False]*(max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)

            print(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdges(0, 1)
g.addEdges(0, 2)
g.addEdges(1, 2)
g.addEdges(2, 0)
g.addEdges(2, 3)
g.addEdges(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFT(2)

