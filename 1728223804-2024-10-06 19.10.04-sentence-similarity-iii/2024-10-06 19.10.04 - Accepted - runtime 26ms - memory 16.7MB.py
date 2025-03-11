class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1, s2 = sentence1.split(), sentence2.split()
        if len(s1) == len(s2): return s1 == s2
        
        # store smaller sentence as s1, and larger as s2
        if len(s1) > len(s2): s1, s2 = s2, s1

        i = 0
        while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
            i += 1
        
        ei, ej = len(s1) - 1, len(s2) - 1
        while ei >= 0 and ej >= 0 and s1[ei] == s2[ej]:
            ei -= 1
            ej -= 1
        j = ei

        # print(i, j)
        return j < i


