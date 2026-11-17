class Twitter:

    def __init__(self):
        self.elapsedTime = 0
        self.follows = defaultdict(set) # follows[user] = set, user follows this set
        self.post = defaultdict(list) # post[user] = post of user

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post[userId].append((self.elapsedTime, tweetId))
        self.elapsedTime += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.follows[userId] #set of people userId follows
        following.add(userId)

        minheap = []
        heapq.heapify(minheap)

        for person in following:

            posts = self.post[person] # list of (time, postid)

            for time, postId in posts:

                if len(minheap) < 10:
                    heapq.heappush(minheap, (time, postId))
                elif time > minheap[0][0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap, (time, postId))
        res = []

        while minheap:
            _, postId = heapq.heappop(minheap)
            res.append(postId)

        return list(reversed(res))


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
