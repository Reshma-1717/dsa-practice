class Solution:
    def dfs(self,node,vis,pathVis,adj,check):
        vis[node] = 1
        pathVis[node] = 1
        check[node] = 0
        for i in adj[node]:
            if vis[i] == 0:
                if self.dfs(i,vis,pathVis,adj,check):
                    return True
            elif pathVis[i] == 1:
                return True
        pathVis[node] = 0
        check[node] = 1
        return False
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        check = [0]*len(graph)
        vis = [0]*len(graph)
        pathVis = [0] * len(graph)

        for i in range(len(graph)):
            if vis[i] == 0:
                self.dfs(i,vis,pathVis,graph,check)
        
        safeNodes = []
        for i in range(len(graph)):
            if check[i] == 1:
                safeNodes.append(i)
        return safeNodes
        