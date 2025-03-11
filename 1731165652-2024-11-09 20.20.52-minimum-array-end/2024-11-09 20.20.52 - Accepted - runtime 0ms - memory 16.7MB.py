class Solution:
    def minEnd(self, n: int, x: int) -> int:
        return self.project(x, n - 1)

    def project(self, x, a):
        i = 0
        while a:
            if (x >> i) & 1:
                i += 1
                continue

            if a & 1:
                x |= (1 << i)

            a >>= 1
            i += 1
        
        return x

        #  111 = 7

        # 0011 AND 0111 AND 1111 = 7
        
        # 0 AND 01
        # x = 5
        # n = 6
        # 101 AND 111 AND 1000 AND 1001 AND 1010 AND 1011


        # 10010
        # 10011
        # 10110
        # 11010
        # 11110
        # 10110
        # 11011
        # 11111

