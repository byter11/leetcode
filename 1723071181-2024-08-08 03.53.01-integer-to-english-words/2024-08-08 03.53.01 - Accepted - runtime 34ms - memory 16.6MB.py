NUMBERS = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

ONE_TEN = {"0": "Ten", "1": "Eleven", "2": "Twelve", "3": "Thirteen", "4": "Fourteen", "5": "Fifteen", "6": "Sixteen", "7": "Seventeen", "8": "Eighteen", "9": "Nineteen"}

OTHER_TEN = {"2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty", "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Ninety"}

UNITS = ["", "Thousand", "Million", "Billion", "Trillion"]

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ans = []
        n = str(num)
        unit = 0
        for i in range(len(n) - 3, -3, -3):
            chunk = ""
            if i < 0:
                chunk = self.convertThree("0"*(-i) + n[:3 - (-i)])
            else:
                chunk = self.convertThree(n[i:i+3])
            
            if chunk:
                if UNITS[unit]: chunk += " " + UNITS[unit]
                ans.append(chunk)
            unit += 1

        return ' '.join(reversed(ans))
    
    def convertThree(self, num: str) -> str:
        # print(num)
        if num == "000":
            return ""
        if num[0] == "0":
            return self.convertTwo(num[1:])
        chunk = NUMBERS[num[0]] + " Hundred"
        if num[1] != "0" or num[2] != "0":
             chunk += " " + self.convertTwo(num[1:])
        return chunk
    
    def convertTwo(self, num: str) -> str:
        if num[0] == "0" and num[1] == "0": return ""
        if num[0] == "0": return NUMBERS[num[1]]
        if num[0] == "1": return ONE_TEN[num[1]]
        if num[1] == "0": return OTHER_TEN[num[0]]
        return OTHER_TEN[num[0]] + " " + NUMBERS[num[1]]
        