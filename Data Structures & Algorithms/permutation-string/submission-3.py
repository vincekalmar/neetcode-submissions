class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count1 = Counter(s1)

        count2 = defaultdict(int)

        l = 0

        for r, c in enumerate(s2):
            print(count2)
            if r - l + 1 > len(s1):
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1
            count2[c] += 1
            if count1 == count2:
                return True
        return False
