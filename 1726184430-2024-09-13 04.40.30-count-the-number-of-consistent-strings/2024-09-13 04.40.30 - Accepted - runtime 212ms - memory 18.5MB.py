class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(list(allowed))

        consistent = 0
        for w in words:
            ok = True
            for c in w:
                if c not in allowed_set:
                    ok = False
                    break
            if ok: consistent += 1
        return consistent
