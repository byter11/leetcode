class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(amnt, letter) for amnt, letter in [(-a, 'a'), (-b, 'b'), (-c, 'c')] if amnt < 0]
        heapq.heapify(heap)

        s = ''
        while heap and heap[0][0] < 0:
            # print(heap)
            i = len(s) - 1
            amnt, cur = heapq.heappop(heap)
            if i > 0 and s[i] == cur and s[i-1] == cur:
                if not heap: break
                a, c = heapq.heappop(heap)
                heapq.heappush(heap, (amnt, cur))
                amnt, cur = a, c
                maxed = ''
            
            s += cur
            # print(s)
            if amnt + 1 < 0:
                heapq.heappush(heap, (amnt + 1, cur))

        return s

# a = 11, b = 1, c = 6
# aaccaaccaaccaabaa