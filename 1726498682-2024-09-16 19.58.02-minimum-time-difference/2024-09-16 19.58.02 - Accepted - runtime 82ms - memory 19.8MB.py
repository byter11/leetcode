class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def mins(a):
            h, m = a.split(':')
            return (int(h) - 1) * 60 + int(m)

        mx = mins("24:59") + 1
        timePoints.sort(key=mins)

        diff = float('inf')
        for i in range(1, len(timePoints)):
            t1, t2 = mins(timePoints[i-1]), mins(timePoints[i])

            diff = min(
                diff, 
                abs(t2 - t1),
                abs(mx - t2) + t1,
                abs(mx - t1) + t2
            )

        return min(diff, abs(mx - mins(timePoints[-1]) + mins(timePoints[0])))
    
