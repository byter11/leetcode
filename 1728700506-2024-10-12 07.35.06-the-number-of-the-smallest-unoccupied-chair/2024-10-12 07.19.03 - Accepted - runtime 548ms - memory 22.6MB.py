class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        target = times[targetFriend]
        times.sort()
        chairs = []
        friends = []
        cur_chair = 0

        for s, e in times:
            while friends and friends[0][0] <= s:
                _, chair = heapq.heappop(friends)
                heapq.heappush(chairs, chair)

            if chairs:
                chair = heapq.heappop(chairs)
            else:
                chair = cur_chair
                cur_chair += 1

            heapq.heappush(friends, (e, chair))
            if s == target[0] and e == target[1]:
                return chair
            
        return 0

