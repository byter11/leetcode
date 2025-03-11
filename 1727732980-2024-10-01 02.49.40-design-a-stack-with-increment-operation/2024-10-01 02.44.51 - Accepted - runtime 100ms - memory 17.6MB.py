class CustomStack:

    def __init__(self, maxSize: int):
        self.st = [0]*maxSize
        self.i = -1
        self.inc = []

    def push(self, x: int) -> None:
        if self.i + 1 >= len(self.st):
            return
        
        self.i += 1
        self.st[self.i] = x

    def pop(self) -> int:
        if self.i == -1:
            return -1
        
        p = self.st[self.i]
        self.i -= 1
        return p

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i > self.i:
                return
            self.st[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)