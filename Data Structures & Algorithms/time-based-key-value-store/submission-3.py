class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list) # key : (time, value)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        arr = self.mp[key]
        if not arr:
            return ""

        l, r = 0, len(arr) - 1
        ans = ""
        while l <= r:
            mid = (l+r) // 2
            
            if arr[mid][0] < timestamp:
                l = mid + 1
                ans = arr[mid][1]
            elif arr[mid][0] > timestamp:
                r = mid - 1
            else:
                return arr[mid][1]

        return ans

