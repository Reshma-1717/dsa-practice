from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 
        m , n = len(grid),len(grid[0])
        total  = 0
        count = 0
        rotten = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    total += 1
                if grid[i][j] == 2:
                    rotten.append((i,j))
        direction = {(0,1),(0,-1),(1,0),(-1,0)}
        day  = 0
        while rotten:
            k = len(rotten)
            count += k
            for _ in range(k):
                x, y = rotten.popleft()

                for dx , dy in direction:
                    nx,ny = x+dx,y+dy

                    if nx <0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != 1:
                        continue

                    grid[nx][ny] = 2

                    rotten.append((nx,ny))
                
            if rotten:
                day += 1
        if count == total:
            return day
        else:
            return -1
                




