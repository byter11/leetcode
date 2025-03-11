class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        w = sum((1 for b in blocks[:k] if b == 'W'))
        ans = w
        for i in range(k, n):
            if blocks[i] == 'W':
                w += 1
            if blocks[i-k] == 'W':
                w -= 1
            ans = min(ans, w)

        return ans