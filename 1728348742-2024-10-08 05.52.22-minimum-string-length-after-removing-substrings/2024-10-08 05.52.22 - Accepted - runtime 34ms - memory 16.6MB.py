class Solution:
    def minLength(self, s: str) -> int:
        n = len(s)

        def can_remove(a, b):
            return (a == 'A' and b == 'B') or (a == 'C' and b == 'D')
        
        st = []
        for c in s:
            if len(st) and can_remove(st[-1], c):
                st.pop()
            else:
                st.append(c)        

        return len(st)
            