class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        g.sort()
        s.sort()
        c = 0
        cookies = len(s) - 1
        child = len(g) - 1
        while cookies >= 0 and child >= 0:
            if s[cookies] >= g[child]:
                c += 1
                cookies -= 1
                child -= 1
            else:
                child -= 1
        return c



class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        c = 0
        till = 0
        tmp = 0
        for x in g:
            for i, y in enumerate(s[till:]):
                if x <= y:
                    c += 1
                    tmp = i
                    break
                tmp = i
            till += tmp + 1
        return c
