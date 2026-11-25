class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for point1 in points:
            for point2 in points:
                point1, point2 = tuple(point1), tuple(point2)
                if point1 != point2:
                    distance = abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
                    adj[point1].append((point2, distance))


        minheap = []
        minheap.append((0, tuple(points[0])))
        heapq.heapify(minheap)
        seen = set()
        res = 0
        while minheap:
            distance, point = heapq.heappop(minheap)

            if point in seen:
                continue

            seen.add(point)
            res += distance

            for neiPoint, cost in adj[point]:
                if neiPoint not in seen:
                    heapq.heappush(minheap, (cost, neiPoint))

        return res

