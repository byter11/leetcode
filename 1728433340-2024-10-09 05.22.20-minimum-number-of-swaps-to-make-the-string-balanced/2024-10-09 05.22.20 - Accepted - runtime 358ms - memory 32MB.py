class Solution:
    def minSwaps(self, s: str) -> int:
        l, n = list(s), len(s)
        opening, ending = 0, 0

        i, j, swaps = 0, len(s) - 1, 0
        while i < j:
            if l[i] == '[': opening += 1
            if l[i] == ']': ending += 1

            if ending > opening:
                while j > i and l[j] != '[': j -= 1
                l[i], l[j] = l[j], l[i]
                opening, ending, swaps = opening + 1, ending - 1, swaps + 1
            
            i += 1
        
        return swaps
