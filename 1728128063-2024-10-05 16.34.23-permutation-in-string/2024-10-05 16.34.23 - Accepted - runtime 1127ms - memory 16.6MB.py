class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        n1, n2 = len(s1), len(s2)
        # print(freq)

        for i in range(len(s2) - n1 + 1):
            ok = True
            # print("comp: ", Counter(s2[i:i+n1]))
            for k, v in Counter(s2[i:i+n1]).items():
                if freq[k] != v:
                    ok = False
                    break
            if ok:
                return True
    
        return False