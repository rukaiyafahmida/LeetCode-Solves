class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counter_1 = 0
        counter_0 = 0
        for x in s:
            if x == '1':
                counter_1 += 1
            else:
                counter_0 += 1
        one = '1'*(counter_1-1)
        zero = '0'*counter_0
        first = "".join(one)
        sec = "".join(zero)
        return first + sec + '1'
