class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = int(len(s))
        l2 = l / 2
        v_list = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        vc_1 = 0
        vc_2 = 0
        for i in range(l):
            if s[i] in v_list:
                if i < l2:
                    vc_1 += 1
                else:
                    vc_2 += 1
        return vc_1 == vc_2
