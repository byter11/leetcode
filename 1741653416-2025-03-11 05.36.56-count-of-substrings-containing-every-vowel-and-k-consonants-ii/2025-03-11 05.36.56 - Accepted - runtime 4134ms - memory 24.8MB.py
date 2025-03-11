class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        n = len(word)
        ans = 0
        i, j = 0, 0
        v = defaultdict(int)
        c = 0
        
        pc = [-1 for _ in range(n)]
        nc = n
        for l in range(n-1, -1, -1):
            pc[l] = nc
            if word[l] not in vowels:
                nc = l
        

        while j < n:
            if word[j] in vowels:
                v[word[j]] += 1
            else:
                c += 1
            
            while c > k:
                if word[i] in vowels:
                    v[word[i]] -= 1
                else:
                    c -= 1
                i += 1
            
            while i < n and all(v[vw] > 0 for vw in vowels) and c == k:
                ans += pc[j] - j
                if word[i] in vowels:
                    v[word[i]] -= 1
                else:
                    c -= 1
                i += 1
            
            j += 1

        return ans