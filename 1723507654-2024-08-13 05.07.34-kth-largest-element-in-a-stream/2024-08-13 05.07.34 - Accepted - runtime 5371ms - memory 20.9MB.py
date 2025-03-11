class KthLargest:

    def __init__(self, k: int, nums: List[int]):
      self.k = k
      self.nums = sorted(nums)
        

    def add(self, val: int) -> int:
        self.nums.append(0)
        i = len(self.nums) - 2
        while i >= 0 and self.nums[i] >= val:
            
            self.nums[i+1] = self.nums[i]
            i -= 1
        self.nums[i+1] = val
        #print(self.nums)
        return self.nums[-self.k]
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)