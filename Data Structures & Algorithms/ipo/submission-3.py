class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        minCapital = [] #minheap for capital (capital, -profit)
        maxProfit = [] #max heap for profit (-profit, capital)

        for profit, cap in zip(profits, capital):
            minCapital.append((cap, -profit))

        heapq.heapify(minCapital)
        currentCapital = w
        while (minCapital or maxProfit) and (k > 0):

            while minCapital and currentCapital >= minCapital[0][0]:
                cap, profit = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, (profit, cap))
            
            if maxProfit:
                profit, cap = heapq.heappop(maxProfit)
                currentCapital += -profit
                k -= 1
            elif minCapital:
                break
                

        return currentCapital
            


        