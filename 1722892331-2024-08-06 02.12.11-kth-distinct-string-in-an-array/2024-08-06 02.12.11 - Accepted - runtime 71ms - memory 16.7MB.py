class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = defaultdict(int)
        for a in arr: count[a] += 1

        i = 0
        for a in arr:
            if count[a] == 1:
                i += 1
            if i == k:
                return a
        return ""