class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        if len([c for c in Counter(s).values() if c % 2 != 0]) > k: return False
        return True 