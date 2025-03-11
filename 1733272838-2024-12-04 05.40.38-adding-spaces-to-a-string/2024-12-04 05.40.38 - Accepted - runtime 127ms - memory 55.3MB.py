class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        spaces = set(spaces)
        a = ""
        for i in range(n):
            if i in spaces:
                a += " "
            a += s[i]
        return a
            