class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        answer = []

        suffixXor = [arr[0]]
        for i in range(1, n):
            suffixXor.append(suffixXor[i-1] ^ arr[i])
        
        for l, r in queries:
            xor = suffixXor[r]
            if l > 0:
                xor ^= suffixXor[l-1]
            answer.append(xor)

        return answer
    

# 0001 0011 0100 1000
#      0011 0111 1111

# 0001 0010 0110 1110