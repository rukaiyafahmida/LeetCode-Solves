class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        c = 0
        for i in range(len_s):
            flag = False
            for j in range(c,len_t):
                a = s[i]
                b = t[j]
                c+=1
                if a == b:
                    flag = True
                    break
            if not flag:
                return False
        return True
