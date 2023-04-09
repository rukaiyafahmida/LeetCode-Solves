class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))>1:
            temp = str(num)
            num = 0
            for c in temp:
                num+=int(c)
        return num
