class ProductOfNumbers:

    def __init__(self):
        self.pp = []

    def add(self, num: int) -> None:
      if num == 0:
        self.pp = [0]*(len(self.pp)+1)
      else:
        self.pp.append(
        ((self.pp[-1] if len(self.pp) else 1) or 1) * num)
        

    def getProduct(self, k: int) -> int:
      if self.pp[-k] == 0:
        return 0
      #print(self.pp, k)
      return int(self.pp[-1] / ((self.pp[-(k+1)] if len(self.pp) > k else 1) or 1))
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)