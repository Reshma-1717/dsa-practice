class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        inicol = image[sr][sc]

        if inicol == color:
            return image
        
        delrow = [-1,0,1,0]
        delcol = [0,1,0,-1]

        def dfs(row,col):
            image[row][col] = color
            n = len(image)
            m = len(image[0])
            for i in range(4):
                nrow = row + delrow[i]
                ncol = col+delcol[i]
                if(0 <= nrow < n and 0 <= ncol < m):
                    if(image[nrow][ncol] == inicol):
                        dfs(nrow,ncol)
        dfs(sr,sc)
        return image
        