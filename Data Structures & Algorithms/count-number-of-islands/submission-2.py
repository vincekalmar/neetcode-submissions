class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen = set()
        res = 0
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        for r, row in enumerate(grid):
            for c, num in enumerate(row):
                if num == '1' and (r,c) not in seen:

                    q = deque()
                    q.append((r,c))
                    seen.add((r,c))

                    while q:
                        x, y = q.popleft()

                        for xd, yd in dirs:
                            nx, ny = x+xd, y+yd
                            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] != '0' and (nx,ny) not in seen:
                                seen.add((nx,ny))
                                q.append((nx,ny))

                    res += 1
        return res



