class Solution:
    cache = {}

    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            bits = self.setbits(nums[i])
            for j in range(i+1, n):
                if nums[j] < nums[i] and self.setbits(nums[j]) != bits:
                    return False
        
        return True


    def setbits(self, n):
        if self.cache.get(n, None):
            return self.cache[n]

        b = n & 1
        while n:
            n >>= 1
            b += n & 1

        self.cache[n] = b
        return b