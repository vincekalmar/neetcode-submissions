class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      
        mp = {}

        for r, num in enumerate(nums):
            
            if num in mp:
                lastSeen = mp[num]
                if r - lastSeen <= k:
                    return True

            mp[num] = r
        

        return False
        


