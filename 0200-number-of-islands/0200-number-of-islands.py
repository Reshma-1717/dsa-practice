class Solution:
    def bfs(self,row,col,grid,vis,delR,delC):
        q = deque()
        q.append((row,col))
        n = len(grid);m = len(grid[0])
        vis[row][col] =1
        while q:
            r, c = q.popleft()
            for i in range(4):
                nrow = r + delR[i]
                ncol = c + delC[i]
                if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == '1' and vis[nrow][ncol] == 0:
                    vis[nrow][ncol] = 1
                    q.append((nrow,ncol))
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid);m = len(grid[0])
        vis = [[0]*m for _ in range(n)]
        delR = [-1,0,1,0]
        delC = [0,1,0,-1]
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and vis[i][j] == 0:
                    cnt += 1
                    self.bfs(i,j,grid,vis,delR,delC)
        return cnt