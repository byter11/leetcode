class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.sieve(left, right + 1)
        ans = [-1, -1]
        mn = float('inf')
        for i in range(len(primes) - 1):
            if primes[i+1] - primes[i] < mn:
                mn = primes[i+1] - primes[i]
                ans = [primes[i], primes[i+1]]

        return ans
    
    def sieve(self, a, n):
        is_prime = [True for i in range(n+1)]
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(sqrt(n) + 1)):
            if not is_prime[i]:
                continue

            for j in range(i*i, n , i):
                is_prime[j] = False

        primes = []
        for i in range(a, n):
            if is_prime[i]: primes.append(i)
        
        return primes