class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        dir = [(-1,0), (1,0), (0,1), (0,-1)]
        seen = set()
        res= 0
        for r, row in enumerate(grid):

            for c, num in enumerate(row):
                
                if num == '1' and (r, c) not in seen:

                    q = deque()
                    q.append((r,c))

                    while q:

                        x, y = q.popleft()
                        for xDir, yDir in dir:
                            newX = xDir + x
                            newY = yDir + y
                            
                            if newX < 0 or newY < 0 or newX >= len(grid) or newY >= len(grid[0]) or grid[newX][newY] == '0' or (newX, newY) in seen:
                                continue
                            seen.add((newX,newY))
                            
                            q.append((newX, newY))
                    res += 1
        return res
            
                        
                

                    


                


        