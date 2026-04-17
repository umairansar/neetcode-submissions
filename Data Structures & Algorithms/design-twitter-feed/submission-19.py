class Twitter:

    def __init__(self):
        self.time = 0
        self.feed = dict()
        self.follows = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed[userId] = self.feed.get(userId, []) + [(-self.time, tweetId)]
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # limit to 10
        maxHeap = [] # maintains heap for all tweets from self and followees

        maxHeap = self.feed.get(userId, []) + [post for followeeId in self.follows.get(userId, []) for post in self.feed.get(followeeId, [])]
        heapq.heapify(maxHeap)

        while len(res) < 10 and maxHeap:
            _, post = heapq.heappop(maxHeap)
            res.append(post)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followeeId not in self.follows.get(followerId, []):
            self.follows[followerId] = self.follows.get(followerId, []) + [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows.get(followerId, []):
            self.follows[followerId].remove(followeeId)

