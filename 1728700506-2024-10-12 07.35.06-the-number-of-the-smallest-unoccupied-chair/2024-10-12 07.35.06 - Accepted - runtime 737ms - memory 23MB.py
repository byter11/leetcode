class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        starts, ends, end = {}, defaultdict(list), 0
        for i, (s, e) in enumerate(times): 
            starts[s] = i
            ends[e].append(i)
            end = max(end, e)

        chairs = [-1]*n
        users = [-1]*n
        minAvailChair = 0
    
        for i in range(end):
            if i in ends:
                for u in ends[i]:
                    chair = users[u]
                    chairs[chair] = -1
                    minAvailChair = min(minAvailChair, chair)

            if i in starts:
                u = starts[i]
                if u == targetFriend: return minAvailChair
                chairs[minAvailChair] = u
                users[u] = minAvailChair
                while chairs[minAvailChair] != -1:
                    minAvailChair += 1

        return -1

