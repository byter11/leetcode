class Solution:
    def clearDigits(self, s: str) -> str:
        l = list(s)
        chars = []
        
        for i, c in enumerate(l):
          if c.isdigit():
            if chars:
              l[chars[-1]] = '*'
              chars.pop()
            l[i] = '*'
          else: chars.append(i)
          
        return ''.join([c for c in l if c != '*'])