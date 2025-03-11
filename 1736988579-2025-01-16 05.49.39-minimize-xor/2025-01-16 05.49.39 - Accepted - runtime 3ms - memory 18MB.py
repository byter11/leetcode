class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # print(bin(num1), bin(num2))
        n = self.bits(num2)
        s = 0
        x = 0
        for i in range(31, -1, -1):
            if (1 << i) & num1 and s < n:
                x = x | (1 << i)
                s += 1

        # print(bin(x), n, s)

        for i in range(n - s):
            x = x | (1 << self.min0(x))
            # print(bin(x))

        
        # print(bin(x), x, x ^ num1)
        return x
    
    def bits(self, x):
        n = 0
        while x:
            if x & 1:
                n += 1
            x >>= 1
        return n

    def min0(self, x):
        i = 0
        while x & 1:
            x >>= 1
            i += 1
        return i
    
# 25, 75
# 0011001 1001000
# x = 0001000
# num2 = 