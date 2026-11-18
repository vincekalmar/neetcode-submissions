class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numToFreq = Counter(nums)

        freqToNum = defaultdict(list)

        for num, freq in numToFreq.items():
            
            freq = numToFreq[num]
            freqToNum[freq].append(num)
        res = []
        print(freqToNum)
        for i in range(len(nums), -1, -1):
            if i in freqToNum:
                for num in freqToNum[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
                    
