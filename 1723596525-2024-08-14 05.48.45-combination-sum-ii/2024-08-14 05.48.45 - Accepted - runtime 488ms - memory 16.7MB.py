class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        visited = set()

        def hash(combination):
            h = [0]*50
            for c in combination: h[c] += 1
            return ''.join([str(i) for i in h])

        def findCombinations(i: int, total: int = 0) -> List[List[int]]:
            if i >= n or total > target:
                return []

            total += candidates[i]
            if total == target:
                return [[candidates[i]]]
            
            combinations = []
            for j in range(i+1, n):
                if j > i + 1 and candidates[j] == candidates[j-1]:
                    continue
                partialCombinations = findCombinations(j, total)
                for c in partialCombinations:
                    combinations.append([candidates[i]] + c)

            return combinations
        
        ans = []
        for i in range(n):
            combinations = findCombinations(i)
            for c in combinations:
                h = hash(c)
                if h in visited:
                    continue
                ans.append(c)
                visited.add(h)

        return ans