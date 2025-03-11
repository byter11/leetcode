class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0]*n
        

        i = n-1 if k > 0 else 0
        d = -1 if k > 0 else 1

        ans = [0]*n
        if k > 0:
            s = 0
            for j in range(k):
                s += code[j]
            
            for i in range(n-1, -1, -1):
                c = code[i]
                ans[i] = s
                s -= code[(i+k)%n]
                s += c
        
        if k < 0:
            i = n + k
            s = 0
            for j in range(i, n):
                s += code[j]

            for i in range(n):
                c = code[i]
                ans[i] = s
                s -= code[(i+k)%n]
                s += c
                # print(s)
            
        return ans
