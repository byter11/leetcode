class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        nums = list(set(nums))
        n = len(nums)
        prods = defaultdict(int)
        for i in range(n):
          for j in range(i+1, n):
            p = nums[i] * nums[j]
            prods[p] += 1
        
        ans = 0
        for p, c in prods.items():
          if c > 1:
            npr = int(nPr(c, 2))
            ans += npr * 4
          
        return ans
        
def nPr(n, r):
  return factorial(n)/factorial(n-r)