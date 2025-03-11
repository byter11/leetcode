class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        n1 = len(words1)
        freqs = [[0]*26 for i in range(n1)]
        for i, w in enumerate(words1):
            for c in w:
                freqs[i][ord(c) - ord('a')] += 1

        freq2 = [0]*26
        for i, w2 in enumerate(words2):
            f = [0]*26
            for c in w2:
                f[ord(c) - ord('a')] += 1

            for j in range(26):
                freq2[j] = max(freq2[j], f[j])
            

        def is_universal(i, w):
            for j in range(26):
                if freqs[i][j] < freq2[j]:
                    return False
            return True

        return [w for i, w in enumerate(words1) if is_universal(i, w)]