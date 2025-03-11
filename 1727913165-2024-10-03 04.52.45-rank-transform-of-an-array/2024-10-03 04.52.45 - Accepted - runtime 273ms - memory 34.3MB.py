class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted([(a, i) for i, a in enumerate(arr)])

        prev = float('inf')
        rank = 0
        for s, i in sorted_arr:
            if s != prev:
                rank += 1
                prev = s
            arr[i] = rank

        return arr