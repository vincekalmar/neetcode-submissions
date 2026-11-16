class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        while l <= r:

            mid = (l+r) // 2

            if self.canEat(mid, piles, h):
                r = mid - 1
            else:
                l = mid + 1
        
        return l


    def canEat(self, eatingRate, piles, h):
        
        time = 0
        for i, pile in enumerate(piles):
            time += math.ceil(pile / eatingRate)

        return time <= h



         