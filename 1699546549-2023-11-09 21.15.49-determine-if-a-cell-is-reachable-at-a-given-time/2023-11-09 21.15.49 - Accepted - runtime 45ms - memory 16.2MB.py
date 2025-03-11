class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t != 1

        dist = max(abs(fy - sy), abs(fx - sx))
        print(dist)

        return t >= dist
