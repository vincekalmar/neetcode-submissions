class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()

        for r, row in enumerate(grid):
            for c, num in enumerate(row):
                if num == 0:
                    q.append((0, r,c))

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            n = len(q)

            for _ in range(n):
                distance, x, y = q.popleft()

                for xd, yd in dirs:
                    nx, ny = x + xd, y + yd

                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == 2147483647:
                        grid[nx][ny] = distance + 1
                        q.append((distance + 1, nx,ny))

        
                        
