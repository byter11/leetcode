class Solution:
    def maximumLength(self, s: str) -> int:
        cur_special = ""
        specials = defaultdict(int)

        for c in s:
            cur_special = c if cur_special == "" or c != cur_special[-1] else cur_special + c

            r = ""
            for a in cur_special:
                r += a
                specials[r] += 1
        
        return len(next(iter(sorted([c for c, f in specials.items() if f >= 3], reverse=True, key = lambda x: len(x))), "")) or -1
        
