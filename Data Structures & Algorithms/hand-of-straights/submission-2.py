class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) // groupSize != len(hand) / groupSize:
            return False

        count = Counter(hand)


        for _ in range(len(hand) // groupSize):
            minNum = min(count)
            for _ in range(groupSize):
                if minNum not in count:
                    return False
                count[minNum] -= 1
                if count[minNum] == 0:
                    del count[minNum]
                minNum += 1

        return True

