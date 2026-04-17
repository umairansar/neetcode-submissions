class Twitter:

    def __init__(self):
        self.posts = dict()
        self.feeds = dict()
        self.followers = dict()
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.posts[userId] = self.posts.get(userId, []) + [(self.time, tweetId)]
        for follower in self.followers.get(userId, []):
            if follower != userId:
                self.feeds[follower] = self.feeds.get(follower, []) + [(self.time, tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:
        return list(map(lambda x:x[1], sorted(self.feeds.get(userId, []) + self.posts.get(userId, []), key=lambda x: x[0], reverse=True)[:10]))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.time += 1
        if followerId in self.followers.get(followeeId, []):
            return
        
        self.followers[followeeId] = self.followers.get(followeeId, []) + [followerId]
        if followeeId != followerId:
            self.feeds[followerId] = self.feeds.get(followerId, []) + self.posts.get(followeeId, [])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.time += 1
        if followerId not in self.followers.get(followeeId, []):
            return

        self.followers[followeeId].remove(followerId)
        if followeeId != followerId:
            self.feeds[followerId] = list(set(self.feeds.get(followerId, [])) - set(self.posts.get(followeeId, [])))        
