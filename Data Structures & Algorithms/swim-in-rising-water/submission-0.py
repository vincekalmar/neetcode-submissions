class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        

        dirs = ((-1,0), (1,0), (0,1), (0,-1))

        minheap = []
        minheap.append((grid[0][0], 0, 0))
        heapq.heapify(minheap)
        seen = set()
        res = 0

        while minheap:
            height, r, c = heapq.heappop(minheap)

            if (r,c) in seen:
                continue
            
            if (r,c) == (len(grid) - 1, len(grid[0]) - 1):
                return max(res, height)

            seen.add((r,c))
            res = max(res, height)

            for x, y in dirs:
                row, col = x+r, y+c
                if 0<=row<len(grid) and 0<=col<len(grid[0]) and (row,col) not in seen:
                    heapq.heappush(minheap, (grid[row][col], row, col))


        return res

