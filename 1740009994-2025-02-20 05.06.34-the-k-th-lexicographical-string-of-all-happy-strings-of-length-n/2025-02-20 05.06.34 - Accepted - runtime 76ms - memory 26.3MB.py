class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        stringset = set()
        
        def generate(s):
          if len(s) == n:
            stringset.add(s)
            return
          
          for c in ['a', 'b', 'c']:
            if len(s) == 0 or s[-1] != c:
              generate(s + c)
        
        generate("")
        sorted_strings = sorted(list(stringset))
        #print(sorted_strings)
        if len(sorted_strings) < k:
          return ""
        return sorted_strings[k-1]
          