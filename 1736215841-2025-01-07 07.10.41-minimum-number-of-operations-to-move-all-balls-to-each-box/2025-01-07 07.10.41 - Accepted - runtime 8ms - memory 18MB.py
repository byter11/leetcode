class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0]*n


        moves_l = 0
        moves_r = 0
        balls_l = 0
        balls_r = 0

        for i in range(n):
            answer[i] += moves_l
            balls_l += int(boxes[i])
            moves_l += balls_l

        
        for i in range(n-1, -1, -1):
            answer[i] += moves_r
            balls_r += int(boxes[i])
            moves_r += balls_r

        return answer