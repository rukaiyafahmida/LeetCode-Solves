class Solution:
    def reverse(self, x: int) -> int:
        int_max = 2 ** 31 - 1
        int_min = -1 * 2 ** 31
        y = str(x)
        if x>=0:
            out= int(y[::-1])
        else:
            z = y[1:]
            out = int(z[::-1]) *-1
        if out >= int_min and out <= int_max :
            return out
        else:
            return 0
