class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s = str(bin(start))[2:]
        g = str(bin(goal))[2:]
        c = 0
        len_s = len(s)
        len_g = len(g)
        if len_s > len_g:
            dif = len_s - len_g
            prefix_g = '0'*dif
            g = prefix_g+g
        elif len_s < len_g:
            dif = len_g - len_s
            prefix_s = '0'*dif
            s = prefix_s+s
        for i in range(len(s)):
            if s[i] != g[i]:
                c+=1
        return c


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start^goal
        c = 0
        s = str(bin(res))[2:]
        print(s)
        for i in range(len(s)):
            if s[i] == '1':
                c+=1
        return c
