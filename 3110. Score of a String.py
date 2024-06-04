class Solution:
    def scoreOfString(self, s: str) -> int:
        out = 0
        for i in range(len(s)-1):
            out += abs(ord(s[i]) - ord(s[i+1]))

        return out








class Solution:
    def scoreOfString(self, s: str) -> int:
        out = 0
        for a, b in zip(s, s[1:]):
            out += abs(ord(a) - ord(b))

        return out
