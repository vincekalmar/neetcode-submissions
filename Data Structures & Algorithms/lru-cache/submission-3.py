class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        value = self.mp[key]
        del self.mp[key]
        self.mp[key] = value

        return self.mp[key]

    def put(self, key: int, value: int) -> None:
        

        if len(self.mp) == self.capacity and key not in self.mp:
            k, v = next(iter(self.mp.items()))
            del self.mp[k]
        if key in self.mp:
            del self.mp[key]
        self.mp[key] = value




    
    