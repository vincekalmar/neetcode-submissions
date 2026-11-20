class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
    
        maxheap = []
        if a != 0: maxheap.append((-a,'a'))
        if b != 0: maxheap.append((-b,'b'))
        if c != 0: maxheap.append((-c,'c'))
        heapq.heapify(maxheap)
        s = []
        while maxheap:

            freq, char = heapq.heappop(maxheap)

            if len(s) >= 2 and char == s[-1] == s[-2]:
                if maxheap:
                    freq2, char2 = heapq.heappop(maxheap)
                    s.append(char2)
                    freq2+=1
                    if freq2 < 0:
                        heapq.heappush(maxheap, (freq2, char2))
                    heapq.heappush(maxheap, (freq, char))
                else:
                    return "".join(s)


            else:
                freq += 1
                s.append(char)
                if freq < 0:
                    heapq.heappush(maxheap, (freq, char))
        
        return "".join(s)


        