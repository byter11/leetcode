class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [ ( -((x[0] + 1) / (x[1] + 1) - (x[0] / x[1])), x) for x in classes]
        heapq.heapify(heap)

        for e in range(extraStudents):
            _, cl = heapq.heappop(heap)
            cl[0], cl[1] = cl[0] + 1, cl[1] + 1
            heapq.heappush(
                heap,
                ( -((cl[0] + 1) / (cl[1] + 1) - (cl[0] / cl[1])), cl)
            )
        
        ans = 0
        for _, cl in heap:
            ans += cl[0] / cl[1]

        return ans / len(classes)

# 3/4 + 3/5 + 2/2 = 2.35
# 1/2 + 5/7 + 2/2 = 2.214
# 1/2 + 3/5 + 4/4 = 2.1