class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        n = len(words)
        # [me, untimeme, meme]
        # meme#untime
        words = sorted([x[::-1] for x in words])
        s = sum([len(x) for x in words]) + n
        
        
        curr = words[n-1]
        for i in range(n-2, -1, -1):
            if curr.startswith(words[i]):
                s -= (len(words[i]) + 1)
            else:
                curr = words[i]
        return s