class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen_A = set()
        seen_B = set()
        common = set()

        ans = [0]*n
        
        for i in range(n):
            if i > 0:
                ans[i] = ans[i-1]

            if B[i] not in seen_B and B[i] not in common:
                seen_B.add(B[i])

            if A[i] in seen_B:
                ans[i] += 1
                seen_B.remove(A[i])
                common.add(A[i])
            
            if A[i] not in seen_A and A[i] not in common:
                seen_A.add(A[i])

            if B[i] in seen_A:
                ans[i] += 1
                seen_A.remove(B[i])
                common.add(B[i])
            
        return ans