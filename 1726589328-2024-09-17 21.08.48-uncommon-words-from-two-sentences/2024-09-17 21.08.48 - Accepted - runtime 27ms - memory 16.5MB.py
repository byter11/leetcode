class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [w for w, c in Counter([c for c in s1.split(' ')] + [c for c in s2.split(' ')]).most_common() if c == 1]