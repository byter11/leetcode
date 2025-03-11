class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        self.nums = []
        for i in range(1, 10):
            self.addStartingWith(i, 0, n)

        return self.nums
        
    def addStartingWith(self, a, n, mx):
        if a > mx: return

        self.nums.append(a)
        for i in range(10):
            self.addStartingWith(a * 10 + i, n + 1, mx)
        
    # 133
    # 1 10 100 11 110