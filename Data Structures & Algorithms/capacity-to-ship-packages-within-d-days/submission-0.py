class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

        l, r = max(weights), sum(weights)
        while l <= r:

            print (l, " ", r)
            mid = (l+r) //2

            if self.canShip(mid, weights, days):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
    

    def canShip(self, capacity, weights, days):

        day = 1
        current = 0
        for weight in weights:
            
            if current + weight > capacity:
                day += 1
                current = weight
            else:
                current += weight
            
        return day <= days