class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k = len(s1)
        if len(s2) < k: return False
        count1 = Counter(s1)
        
        count2 = defaultdict(int)

        l, r = 0, 0

        for r in range(k):
            count2[s2[r]] += 1
        
        if count1 == count2:
            return True
        

        for r in range(r+1, len(s2)):
            print(count2)
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                del count2[s2[l]]
            l+=1
            count2[s2[r]] += 1

            if count1 == count2:
                return True
        
        return False

        
