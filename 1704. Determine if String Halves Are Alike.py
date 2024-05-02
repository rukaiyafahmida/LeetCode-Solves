class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)
        v_list = "aeiouAEIOU"
        vc_1 = 0
        vc_2 = 0
        for i in range(l // 2):
            if s[i] in v_list:
                vc_1 += 1
            if s[l-i-1] in v_list:
                vc_2 += 1
        return vc_1 == vc_2
