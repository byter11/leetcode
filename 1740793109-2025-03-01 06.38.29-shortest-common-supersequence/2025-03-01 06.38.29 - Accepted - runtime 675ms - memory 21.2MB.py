class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        prev = [str2[0:i] for i in range(m + 1)]

        for i in range(1, n+1):
            cur = [str1[0:i]] + [None for _ in range(m)]

            for j in range(1, m + 1):
                if str1[i-1] == str2[j-1]:
                    cur[j] = prev[j-1] + str1[i-1]
                else:
                    cur[j] = (
                        prev[j] + str1[i-1]
                        if len(prev[j]) < len(cur[j-1])
                        else cur[j-1] + str2[j-1]
                    )

            prev = cur

        return prev[m]