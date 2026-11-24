class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        l, r = 0, mountainArr.length() - 1
        peakIndex = 0
        while l <= r:
            mid = (l+r) // 2

            curr = mountainArr.get(mid)
            currNext = mountainArr.get(mid+1)
            if mountainArr.get(mid-1) < curr  and curr > currNext:
                if curr == target: return mid
                peakIndex = mid
                break
            elif curr < currNext:
                l = mid + 1
            else:
                r = mid -1
        
        l, r = 0, peakIndex - 1

        while l <= r:
            mid = (l+r) // 2

            curr = mountainArr.get(mid)

            if curr < target:
                l = mid + 1
            elif curr > target:
                r = mid - 1
            else:
                return mid
        
        l, r = peakIndex + 1, mountainArr.length() - 1

        while l <= r:
            mid = (l+r) // 2

            curr = mountainArr.get(mid)

            if curr > target:
                l = mid + 1
            elif curr < target:
                r = mid - 1
            else:
                return mid
        return -1 




