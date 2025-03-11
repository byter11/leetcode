class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        a, b = -1, -1
        
        for row in grid:
            for num in row:
                if num in seen:
                    a = num
                seen.add(num)
        
        for num in range(1, len(grid)**2 + 1):
            if num not in seen:
                b = num
                break
            
        return [a,b]