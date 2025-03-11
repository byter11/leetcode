class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ans = 2
        numset = set(arr)

        dp = {}

        def search(n, a):
            if (n, a) in dp:
                return dp[(n,a)]
            b = n-a
            if b in numset and b < a:
                # print(n, a, b)
                dp[(n, a)] = 1 + search(a, b)
                return dp[(n,a)]
            return 2

        for i in range(len(arr)-1, 1, -1):
            for j in range(i-1, 0, -1):
                a, b = arr[i], arr[j]
                ans = max(ans, search(a, b))

        if ans <= 2:
            return 0
            
        return ans

# [1,2,3] = 3
# [1] = 0
# [1,2] = 0
# [1,2,3] = 3
# [1,2,3,4] = 3
# [1,2,3,4,7] = 4
