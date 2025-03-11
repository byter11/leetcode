class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        p = list(s)
        for i, c in enumerate(locked): 
            if c == '0': p[i] = '*'
        
        def resolve(p):
            st = []
            stw = []
            for i, c in enumerate(p):
                if c == '(' :
                    st.append(i)

                if c == '*':
                    stw.append(i)

                if c == ')':
                    if st: st.pop()
                    elif stw: stw.pop()
                    else: return False, st, stw

            return True, st, stw

        ok, st, stw = resolve(p)
        if not ok: return False

        while st and stw and st[-1] < stw[-1]:
            st.pop()
            stw.pop()

        return not st