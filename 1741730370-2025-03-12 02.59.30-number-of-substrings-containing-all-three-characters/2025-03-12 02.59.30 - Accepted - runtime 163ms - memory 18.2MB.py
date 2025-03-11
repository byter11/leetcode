class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        freqs = [0, 0, 0]
        i = 0
        ans = 0
        last = [-1, -1, -1]

        for i in range(n):
            jdx = ord(s[i]) - ord('a')
            kdx, ok = i, True

            for j in range(3):
                if jdx == j: continue

                if last[j] == -1:
                    ok = False
                    break
                kdx = min(kdx, last[j])

            if ok:
                # print(i, kdx+1, last)
                ans += kdx + 1

            last[jdx] = i
        
        return ans

    # bacabc