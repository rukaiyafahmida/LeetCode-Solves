class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        five = 0
        ten = 0
        twenty = 0
        for m in bills:
            if m == 5:
                five += 1
                continue
            if m == 10:
                ten += 1
                if five > 0:
                    five -= 1
                    continue
                return False
            if m == 20:
                twenty += 1
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                    continue
                if five > 2:
                    five -= 3
                    continue
                return False
        return True
