class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        for i in range(1, n):
            if number[i-1] == digit and number[i] > number[i-1]:
                if i == 1:
                    return number[i:]
                return number[:i-1] + number[i:]
        
        for i in range(n-1, -1, -1):
            if number[i] == digit:
                return number[:i] + number[i+1:]
            
        return number
            