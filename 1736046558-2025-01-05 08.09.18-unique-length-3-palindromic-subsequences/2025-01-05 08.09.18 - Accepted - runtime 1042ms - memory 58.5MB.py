class Solution:
    def _init_suffix_freq(self, s):
        n = len(s)
        self.suffix_freq = [[0]*26 for i in range(n)]

        self.suffix_freq[n-1][ord(s[-1]) - ord('a')] = 1
        
        for i in range(n-2, -1, -1):
            self.suffix_freq[i] = [f for f in self.suffix_freq[i+1]]
            self.suffix_freq[i][ord(s[i]) - ord('a')] += 1
        
    def _init_atoi(self, s):
        self.atoi = defaultdict(list)
        for i, c in enumerate(s):
            self.atoi[c].append(i)
    
    def _pair(self, a: str, i: int):
        return max(self.atoi[a])
        
    def _unique_chars(self, i: int, j: int) -> set:
        freqs = [f for f in self.suffix_freq[i]]
        for k, f in enumerate(self.suffix_freq[j]):
            freqs[k] -= f
        
        return set([chr(x + ord('a')) for x, f in enumerate(freqs) if f > 0])

    def countPalindromicSubsequence(self, s: str) -> int:
        self._init_suffix_freq(s)
        self._init_atoi(s)

        ans = 0
        ans = set()
        done = set()
        for i, a in enumerate(s):
            if a in done:
                continue
            done.add(a)
            
            j = self._pair(a, i)
            if i == j:
                continue

            for v in self._unique_chars(i+1, j):
                # print(i, j, a + v + a)
                ans.add(a + v + a)

        return len(ans)

            
    
            
