class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def helper(left):
            if left == 0:
                return 0
            if left in cache: return cache[left]
            
            cache[left] = float('inf')
            for coin in coins:
                if left >= coin:
                    cache[left] = min(cache[left], helper(left - coin) + 1)

            return cache[left]
        
        ans = helper(amount)
        if ans == float('inf'): return -1
        return ans