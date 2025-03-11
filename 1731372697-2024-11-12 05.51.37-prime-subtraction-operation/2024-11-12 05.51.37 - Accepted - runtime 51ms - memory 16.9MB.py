class Solution:
    def __init__(self):
        self.primes = {}

    def largest_prime(self, a):
        while a >= 2:
            if not self.primes.get(a, None):
                self.primes[a] = self.is_prime(a)

            if self.primes[a]:
                return a
            a -= 1

        return a

    def is_prime(self, a):
        for i in range(2,int(a/2)+1):
            if a % i == 0:
                return False

        # print(a, "is prime")
        return True

    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)
        prev = 0
        for a in nums:
            if a <= prev:
                return False

            if a - prev > 2:
                # print(prev, a, self.largest_prime(a - prev - 1))
                prev = a - self.largest_prime(a - prev - 1)
            else:
                prev = a
            # print(prev)
        return True
    
    # 5 13 4 13
    # 2 