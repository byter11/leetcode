class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        answer = []

        prefixXor = [arr[0]]
        for i in range(1, n):
            prefixXor.append(prefixXor[i-1] ^ arr[i])
        
        for l, r in queries:
            xor = prefixXor[r]
            if l > 0:
                xor ^= prefixXor[l-1]
            answer.append(xor)

        return answer
    

# 0001 0011 0100 1000
#      0011 0111 1111

# 0001 0010 0110 1110