class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st = []
        for c in s:
            st.append(c)
            if len(st) >= len(part) and ''.join(st[-len(part):]) == part:
                for i in range(len(part)): st.pop()
                    
        return ''.join(st)