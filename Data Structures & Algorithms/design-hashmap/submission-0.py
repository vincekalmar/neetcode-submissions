class MyHashMap:

    def __init__(self):
        self.size = 1009
        self.bucket = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        for i, (k, v) in enumerate(self.bucket[index]):
            if k == key:
                self.bucket[index][i] = (key, value)
                return

        self.bucket[index].append((key, value))

    def get(self, key: int) -> int:
        index = key % self.size
        
        for k, v in self.bucket[index]:
            if k == key:
                return v

        return -1

        

    def remove(self, key: int) -> None:
        index = key % self.size
        
        for k, v in self.bucket[index]:
            if k == key:
                self.bucket[index].remove((k,v))
                


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)