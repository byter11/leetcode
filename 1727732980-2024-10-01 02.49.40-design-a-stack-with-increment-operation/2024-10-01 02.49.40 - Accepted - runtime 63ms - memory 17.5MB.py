class CustomStack:

    def __init__(self, maxSize: int):
        self.st = [0]*maxSize
        self.i = -1
        self.inc = [0]*maxSize

    def push(self, x: int) -> None:
        if self.i + 1 >= len(self.st):
            return
        
        self.i += 1
        self.st[self.i] = x

    def pop(self) -> int:
        if self.i == -1:
            return -1
        
        p = self.st[self.i]
        p += self.inc[self.i]

        if self.i > 0:
            self.inc[self.i-1] += self.inc[self.i]

        self.inc[self.i] = 0
        self.i -= 1
        return p

    def increment(self, k: int, val: int) -> None:
        if self.i >= 0:
            self.inc[min(self.i, k - 1)] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)