class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        marked_s = [[c, 0] for c in s]

        for st, e, d in shifts:
            if d == 0: d = -1
            marked_s[st][1] += d
            if e < len(s) - 1:
                marked_s[e+1][1] -= d

        # print(marked_s)

        shift = 0
        for i in range(len(s)):
            shift += marked_s[i][1]
            marked_s[i][0] = chr( ((ord(s[i]) - ord('a') + shift) % 26) + ord('a') )

        return ''.join([c for c, shift in marked_s])