class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            x = i * i
            if self.can_partition(str(x), i):
                # print(i, x)
                ans += x
        return ans    

    @lru_cache
    def can_partition(self, x: str, left: int):
        arr = list(x)
        if left == 0 and len(arr) == 0:
            return True
        
        if left < 0:
            return False

        for i, x in enumerate(arr):
            if self.can_partition(
                ''.join(arr[i+1:]),
                left - int(''.join(arr[:i+1]))
            ):
                return True
        
        return False

