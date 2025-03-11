class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = set(nums)
        for i in range(1, len(n)+2):
            if i not in n:
                return i
        
        return len(n)+1