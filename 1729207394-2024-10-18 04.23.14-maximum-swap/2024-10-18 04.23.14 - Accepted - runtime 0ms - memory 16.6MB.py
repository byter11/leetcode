class Solution:
    def maximumSwap(self, num: int) -> int:
        l = list(map(int, str(num)))
        n = len(l)

        suffix_max = [l[n-1]] * n
        prefix_min = [l[0]] * n

        for i in range(n-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], l[i])

        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i-1], l[i])
        
        left_most_min = 1e9+7
        right_most_max = 0
        for i in range(n):
            mn, mx = prefix_min[i], suffix_max[i]
            if mx > mn:
                left_most_min = mn
                right_most_max = mx
                break
        
        # print(left_most_min, right_most_max)
        if left_most_min > right_most_max:
            return int(''.join(map(str, l)))

        a, b = 0, n - 1
        for i in range(n):
            if right_most_max == l[i]: 
                a = i

        for i in range(n-1, -1, -1):
            if left_most_min == l[i]: 
                b = i

        l[a], l[b] = l[b], l[a]

        return int(''.join(map(str, l)))