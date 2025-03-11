class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        freq = defaultdict(int)

        for a in arr:
            rem = a % k
            if rem < 0: rem += k
            freq[rem] += 1
        
        for a in arr:
            rem = a % k
            if rem < 0: rem += k
            
            if rem == 0:
                if freq[rem] % 2 == 1: return False
            elif freq[rem] != freq[k - rem]: return False
        
        return True