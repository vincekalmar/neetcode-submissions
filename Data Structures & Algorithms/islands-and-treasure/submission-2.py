class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        dir = [(-1,0), (1,0), (0,1), (0,-1)]
        q = deque()
        for r, row in enumerate(grid):
            for c, num in enumerate(row):
                if num == 0: 
                    q.append((r,c,0))

        while q:
            x,y,distance = q.popleft()

            for xd, yd in dir:
                newx = xd + x
                newy = yd + y
                if self.inBounds(newx,newy,grid):
                    q.append((newx,newy, distance + 1))
                    grid[newx][newy] = min(grid[newx][newy], distance + 1)

    

    def inBounds(self,r,c,grid):

        return 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] == 2147483647






