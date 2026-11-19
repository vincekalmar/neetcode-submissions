class LRUCache:

    def __init__(self, capacity: int):
       self.mp = {}
       self.capacity = capacity

    def get(self, key: int) -> int:
        value = -1
        if key in self.mp:
            value = self.mp[key]   
            del self.mp[key]
        else:
            return -1
        
        self.mp[key] = value
        return value
       
    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            del self.mp[key]
        elif self.capacity == len(self.mp):
            first_key = next(iter(self.mp))
            del self.mp[first_key]

        
        self.mp[key] = value
