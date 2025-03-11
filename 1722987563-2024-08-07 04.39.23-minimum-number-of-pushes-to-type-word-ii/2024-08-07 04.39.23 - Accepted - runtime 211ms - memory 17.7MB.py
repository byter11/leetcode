class Solution:
    def minimumPushes(self, word: str) -> int:
        count = defaultdict(int)
        for w in word: count[w] += 1

        s = []
        for w in count:
            s.append((count[w], w))
        s.sort()
        s.reverse()

        ans = 0
        col = 1
        for i, (c, w) in enumerate(s):
            if i != 0 and i % 8 == 0:
                col += 1
            ans += c * col
            # print(i, c, w)

        return ans
        
