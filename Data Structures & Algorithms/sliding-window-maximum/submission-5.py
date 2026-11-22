class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maxheap = []
        heapq.heapify(maxheap)
        res = []
        l = r = 0
        for r, num in enumerate(nums):

            if len(maxheap) < k:
                heapq.heappush(maxheap,(-nums[r],r))
            else:
                while l > maxheap[0][1]:
                    heapq.heappop(maxheap)

                res.append(-maxheap[0][0])

                heapq.heappush(maxheap, (-nums[r], r))

                l+=1
        while l > maxheap[0][1]:
                    heapq.heappop(maxheap)
        res.append(-heapq.heappop(maxheap)[0])

        return res

            


