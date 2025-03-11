class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])
        row = points[0]

        for i in range(1, n):
            left = [points[i-1][0]]
            for j in range(1, m): left.append(max(left[j-1] - 1, points[i-1][j]))

            right = [points[i-1][-1]]
            for j in range(m - 2, -1, -1): right.append(max(right[m-j-2] - 1, points[i-1][j]))
            right.reverse()

            for j in range(m):
                points[i][j] = points[i][j] + max(left[j], right[j])

        return max(points[-1])
