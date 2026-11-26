class FreqStack:

    def __init__(self):
        self.stackMap = defaultdict(list) 
        self.freq = defaultdict(int)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.stackMap[self.freq[val]].append(val)
        if self.freq[val] > self.maxFreq:
            self.maxFreq = max(self.maxFreq, self.freq[val])



    def pop(self) -> int:
        res = self.stackMap[self.maxFreq].pop()
        self.freq[res] -= 1
        if not self.stackMap[self.maxFreq]:
            self.maxFreq -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()