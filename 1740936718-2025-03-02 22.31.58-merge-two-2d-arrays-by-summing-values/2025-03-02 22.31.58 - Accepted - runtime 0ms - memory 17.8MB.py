class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j, n, m = 0, 0, len(nums1), len(nums2)
        ans = []
        while i < n and j < m:
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]

            if id1 == id2:
                ans.append([id1, val1 + val2])
                i += 1
                j += 1
            if id1 < id2:
                ans.append(nums1[i])
                i += 1
            if id1 > id2:
                ans.append(nums2[j])
                j += 1
        
        while i < n:
            ans.append(nums1[i])
            i += 1
        
        while j < m:
            ans.append(nums2[j])
            j += 1
        
        return ans