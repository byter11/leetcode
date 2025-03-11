class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
    
        return self.say(self.countAndSay(n-1))
        
    def say(self, num):
        c = 1
        prev = num[0]
        s = ""
        for i in num[1:]:
            if i != prev:
                s += str(c)+prev
                c = 0
            prev = i
            c += 1
            
        s += str(c)+prev
            
        return s