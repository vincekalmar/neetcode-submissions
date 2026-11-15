class MyHashSet:

    def __init__(self):
        self.size = 1009
        self.bucket = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        loc = key % self.size

        if key not in self.bucket[loc]:
            self.bucket[loc].append(key)

    def remove(self, key: int) -> None:
        loc = key % self.size

        if key in self.bucket[loc]:
            self.bucket[loc].remove(key)
        
    def contains(self, key: int) -> bool:
        loc = key % self.size

        return key in self.bucket[loc]

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)