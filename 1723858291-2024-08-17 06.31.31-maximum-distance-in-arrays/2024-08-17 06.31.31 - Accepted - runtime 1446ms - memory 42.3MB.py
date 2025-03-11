class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mn, mni = min([ [a[0], i] for i, a in enumerate(arrays)])
        otherMx, _ = max([ [a[len(a)-1], i] for i, a in enumerate(arrays) if i != mni ])

        mx, mxi = max([ [a[len(a)-1], i] for i, a in enumerate(arrays)])
        otherMn, _ = min([ [a[0], i] for i, a in enumerate(arrays) if i != mxi ])

        return max(abs(mx - otherMn), abs(otherMx - mn))