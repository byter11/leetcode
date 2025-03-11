class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a = "ab"
        b = "ba"
        if y > x:
            x, y = y, x
            a, b = b, a

        st = []
        points = 0
        for c in s:
            if st and st[-1] == a[0] and c == a[1]:
                st.pop()
                points += x
            else:
                st.append(c)

        st2 = []
        for c in st:
            if st2 and st2[-1] == b[0] and c == b[1]:
                st2.pop()
                points += y
            else:
                st2.append(c)

        # print(st)
        return points
