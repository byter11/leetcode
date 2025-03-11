class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return str(int(''.join(sorted(map(str, nums), key=cmp_to_key(lambda x, y: int(y + x) - int(x + y))))))