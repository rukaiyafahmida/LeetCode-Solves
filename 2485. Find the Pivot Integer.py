class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        temp1 = 0
        temp2 = 0
        s1 = []
        s2 = []
        for i in range(1, n + 1):
            temp1 += i
            temp2 += n + 1 - i
            key1 = {temp1: i}
            key2 = {temp2: n + 1 - i}
            s1.append(key1)
            s2.append(key2)
            if key1 in s2 and key1 in s1:
                return i
        return -1
