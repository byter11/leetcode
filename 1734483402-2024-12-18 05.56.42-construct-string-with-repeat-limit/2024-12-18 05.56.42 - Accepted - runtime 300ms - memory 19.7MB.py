class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = dict(Counter(s))
        
        ans = []
        pq = [(-ord(c), c) for c in list(set(s))]
        heapq.heapify(pq)

        while pq:
            o, c = heapq.heappop(pq)
            count = freq[c]

            freq[c] -= min(repeatLimit, freq[c])
            for i in range(min(repeatLimit, count)):
                ans.append(c)

            if pq and count > repeatLimit:
                o2, c2 = heapq.heappop(pq)
                ans.append(c2)
                freq[c2] -= 1
                if freq[c2]:
                    heapq.heappush(pq, (o2, c2))
                heapq.heappush(pq, (o, c))

        return ''.join(ans)




