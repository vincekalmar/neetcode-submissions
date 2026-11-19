class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        l, r = 0, len(people) - 1

        weight = 0
        boat = 0
        onBoat = 0
        while l<=r:
            
            while l<=r and onBoat < 2 and weight + people[r] <= limit:
                weight += people[r]
                onBoat += 1
                r-=1
            
            while l<r and onBoat < 2 and weight + people[l] <= limit:
                weight += people[l]
                l+=1
                onBoat += 1
            
            weight = 0
            boat += 1
            onBoat = 0

        return boat

