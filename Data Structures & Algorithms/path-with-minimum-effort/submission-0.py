class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        

        dirs = [(-1,0), (1,0), (0,1), (0,-1)]

        minheap = []
        heapq.heapify(minheap)
        minheap.append((0,0,0)) #cost, r, c
        seen = {}
        seen[(0,0)] = 0
        while minheap:

            maxEffort, r, c = heapq.heappop(minheap)
            if r == len(heights) - 1 and c == len(heights[0]) - 1:
                return maxEffort

            for x, y in dirs:
                nr, nc = r + x, c + y
                if 0<=nr<len(heights) and 0<=nc<len(heights[0]) and ((nr,nc) not in seen or maxEffort < seen[(nr,nc)]):               
                    effort = abs(heights[nr][nc] - heights[r][c])
                    seen[nr,nc] = max(effort, maxEffort)
                    heapq.heappush(minheap, (max(effort, maxEffort), nr, nc))



        