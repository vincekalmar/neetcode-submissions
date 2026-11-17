class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        seen = set()
        dir = [(-1,0), (1,0), (0,1), (0,-1)]
        res = 0

        for r, row in enumerate(grid):
            for c, num in enumerate(row):

                if num == 1 and (r,c) not in seen:
                    q = deque()
                    q.append((r,c))
                    currentArea = 1
                    seen.add((r,c))

                    while q:

                        x,y = q.popleft()

                        for xdir, ydir in dir:
                            newx = xdir + x
                            newy = ydir + y
                            if len(grid) <= newx or newx < 0 or len(grid[0]) <= newy or newy < 0 or grid[newx][newy] == 0 or (newx,newy) in seen:
                                continue
                            currentArea += 1
                            seen.add((newx,newy))
                            q.append((newx,newy))
                    res = max(currentArea, res)

        return res


