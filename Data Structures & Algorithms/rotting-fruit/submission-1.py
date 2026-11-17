class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        q = deque()
        fresh = 0
        for r, row in enumerate(grid):
            for c, num in enumerate(row):
                if num == 2:
                    q.append((r,c))
                if num == 1:
                    fresh+=1

        dir = [(-1,0), (1,0), (0,1), (0,-1)]
        timeElapsed = 0
        while q and fresh > 0:

            n = len(q)
            
            for _ in range(n):
                x,y = q.popleft()

                for xd, yd in dir:
                    newx = xd + x
                    newy = yd + y

                    if self.canEnque(newx,newy,grid):
                        q.append((newx,newy))
                        grid[newx][newy] = 2
                        fresh -= 1

            timeElapsed += 1
        
        return timeElapsed if fresh == 0 else -1
    
    def canEnque(self, r,c, grid):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1


        

