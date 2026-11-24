class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        l, r = min(nums), sum(nums)

        while l <= r:

            mid = (l+r) // 2

            if self.canSplit(mid, nums, k):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
        

    def canSplit(self, largestSum, nums, numSplits):
        total = 0
        splitCount = 1
        for num in nums:
            if num > largestSum:
                return False
            if total + num > largestSum:
                splitCount += 1
                total = 0
            total += num
        if total > largestSum: return False
        print(largestSum, splitCount, numSplits)
        return splitCount <= numSplits










