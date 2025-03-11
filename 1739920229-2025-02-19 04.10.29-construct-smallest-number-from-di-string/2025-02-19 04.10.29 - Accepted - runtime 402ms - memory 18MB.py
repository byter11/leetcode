MAX_NUM = '9999999999'
class Solution:
    MAX_NUM = "9999999999"
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        taken = [False]*10
        
        def dfs(j, cur):
          if len(cur) == n+1:
            return cur
          
          num = MAX_NUM
          incr = pattern[j] == 'I'
          for i in range(1, 10):
            if taken[i] == True:
              continue
            taken[i] = True
            if (incr and i > int(cur[-1])) or (not incr and i < int(cur[-1])):
              num = min(num, dfs(j+1, cur + str(i)))
            taken[i] = False
           
          return num
         
        num = MAX_NUM
        for i in range(1,10):
          taken[i] = True
          c = dfs(0, str(i))
          taken[i] = False
          if c != MAX_NUM:
            num = min(num, c)
        return num
              
            
            
