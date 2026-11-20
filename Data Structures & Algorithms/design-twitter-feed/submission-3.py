class Twitter:

    def __init__(self):
        self.follows = defaultdict(set) 
        self.usersPost = defaultdict(list)
        self.elapsedTime = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.usersPost[userId].append((self.elapsedTime, tweetId))
        self.elapsedTime += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        posters = self.follows[userId]
        posters.add(userId)

        minheap = []
        heapq.heapify(minheap)

        for user in posters:
            for time, tweetId in self.usersPost[user]:
                if len(minheap) < 10:
                    heapq.heappush(minheap, (time, tweetId))
                elif time > minheap[0][0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap, (time, tweetId))
        res = []
        while minheap:
            _, tweetId = heapq.heappop(minheap)
            res.append(tweetId)
        return list(reversed(res))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)