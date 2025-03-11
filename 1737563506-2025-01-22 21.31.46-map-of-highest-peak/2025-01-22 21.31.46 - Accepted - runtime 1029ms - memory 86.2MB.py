class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        heights = [[0]*m for _ in range(n)]
        q = deque()
        for i, r in enumerate(isWater):
            for j, c in enumerate(r):
                if c == 1:
                    q.append((i, j, 0))

        while q:
            i, j, h = q.popleft()
            if heights[i][j]:
                continue
                
            heights [i][j] = h

            for k, l in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if k < 0 or l < 0 or k >= n or l >= m:
                    continue

                if heights[k][l]:
                    continue
                
                if isWater[k][l]:
                    continue

                q.append((k, l, 0 if isWater[k][l] else h + 1))
        
        return heights

# [1,2,0],
# [0,1,2],
# [1,2,2]