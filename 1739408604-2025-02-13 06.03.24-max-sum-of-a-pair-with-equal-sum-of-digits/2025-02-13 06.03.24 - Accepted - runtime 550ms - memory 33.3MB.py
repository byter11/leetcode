class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sums = defaultdict(list)
       
        for n in nums:
          heapq.heappush(sums[sum([int(c) for c in str(n)])], -n)
         
        filtered_sum = [(s,c) for s,c in sums.items() if len(c) >= 2]

        
        ans = -1
        for s, l in filtered_sum:
          ans = max(ans, -heapq.heappop(l) + -heapq.heappop(l))
         
        return ans