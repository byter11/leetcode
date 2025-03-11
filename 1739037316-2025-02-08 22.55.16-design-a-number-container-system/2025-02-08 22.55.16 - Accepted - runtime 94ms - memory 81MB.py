class NumberContainers:
    def __init__(self):
        self.nums = defaultdict(list)
        self.indexes = {}


    def change(self, index: int, number: int) -> None:
        self.indexes[index] = number
        heapq.heappush(self.nums[number], index)

    def find(self, number: int) -> int:
        heap = self.nums[number]
        while heap:
            min_idx = heap[0]
            if self.indexes[min_idx] == number:
                return min_idx
            heapq.heappop(heap)

        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)