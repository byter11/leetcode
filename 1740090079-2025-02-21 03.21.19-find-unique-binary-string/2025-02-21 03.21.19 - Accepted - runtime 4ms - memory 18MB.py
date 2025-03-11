class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
      s = set(nums)
      n = len(nums[0])
      def find(cur):
        if len(cur) == n:
          if cur not in s: return cur
          return ""
        c = find(cur +'0')
        if c:
          return c
        
        return find(cur + '1')
      
      return find("")
       