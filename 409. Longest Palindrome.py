class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        val = c.values()
        is_odd = False
        out = 0
        for v in val:
            if v % 2 == 0:
                out += v
            else:
                out += v-1
                is_odd = True
        return out+1 if is_odd else out
