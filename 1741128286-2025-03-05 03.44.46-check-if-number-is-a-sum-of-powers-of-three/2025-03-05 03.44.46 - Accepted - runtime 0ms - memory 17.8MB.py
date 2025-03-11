class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ternary = []
        while n:
            ternary.append(n % 3)
            n //= 3
        
        return 2 not in ternary