class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        for b in bills:
            #print(change)
            change[b] += 1
            b -= 5
            #print(b, b // 5)
            if b == 0:
                continue
            if b >= 10 and change[10]:
                change[10] -= 1
                b -= 10
            if b//5 <= change[5]:
                change[5] -= b//5
                b = 0
            elif b > 0: 
                return False
                
        #print(change)
        return True