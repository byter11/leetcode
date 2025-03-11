class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr = sorted([(str(s), True) for s in arr1] 
        + [(str(s), False) for s in arr2])

        print(arr)
        i, last, last_typ = 1, arr[0][0], arr[0][1]
        mx = 0
        while i < len(arr):
            s1, typ1 = arr[i-1]
            s2, typ2 = arr[i]
            if typ1 == typ2:
                last = s2
            elif typ2 != last_typ:
                mx = max(mx, self.lcp(last, s2))
            else:
                last = s1
                last_typ = typ1
                mx = max(mx, self.lcp(last, s2))
            i += 1
        
        return mx
    
    def lcp(self, a, b):
        i, res = 0, 0
        while i < len(a) and i < len(b) and a[i] == b[i]: i += 1
        return i
            
