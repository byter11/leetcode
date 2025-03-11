class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        freq = defaultdict(int)

        for a in arr:
            freq[ ( a % k + k ) % k ] += 1
        
        for a in arr:
            rem = (a % k + k) % k
            if rem == 0:
                if freq[rem] % 2 == 1: return False
            elif freq[rem] != freq[k - rem]: return False
        
        return True