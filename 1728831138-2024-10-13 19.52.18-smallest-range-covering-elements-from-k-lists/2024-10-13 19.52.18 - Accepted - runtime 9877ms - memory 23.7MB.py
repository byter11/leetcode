class CoverState:
    def __init__(self, nums):
        self.num_map = {}
        self.lst_sizes = [0 for n in nums]
        self.min, self.max = float('inf'), -float('inf')
        for i, lst in enumerate(nums):
            for n in lst:
                if not self.num_map.get(n): self.num_map[n] = []
                self.num_map[n].append(i)
                self.min, self.max = min(self.min, n), max(self.max, n)

    def shrink(self, i):
        for n in self.num_map.get(i, []):
            self.lst_sizes[n] -= 1
            
    def expand(self, i):
        for n in self.num_map.get(i, []):
            self.lst_sizes[n] += 1
    
    def valid(self):
        return not any(n == 0 for n in self.lst_sizes)

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        state = CoverState(nums)

        merged = []
        for lst in nums:
            for n in lst:
                merged.append(n)
        merged.sort()

        i = 0
        best_state = (state.min, state.max)

        # slide the window
        for j in merged:
            state.expand(j)
            # print("expand", merged[i], j)

            # shrink while valid
            while i < len(merged) and merged[i] <= j and state.valid():
                state.shrink(merged[i])
                # print("shrink", merged[i], j)
                i += 1


            # print("cmp ", (merged[i-1], j), best_state)
            if i > 0 and self.cmp_state((merged[i-1], j), best_state) == -1:
                best_state = (merged[i-1], j)

        # print(best_state)
        return best_state
    
    def cmp_state(self, a, b):
        if a[1] - a[0] == b[1] - b[0]:
            return -1 if a[1] < b[1] else 1

        return -1 if a[1] - a[0] < b[1] - b[0] else 1
