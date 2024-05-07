class Solution:
    def minimumPushes(self, word: str) -> int:
        l = len(word)
        out = 0
        i = 1
        while l > 0:
            x = min(8, l)
            out += x * i
            l -= 8
            i += 1

        return out


class Solution:
    def minimumPushes(self, word: str) -> int:
        l = len(word)
        out = 0
        i = 1
        while l > 0:
            if l >= 8:
                out += 8 * i
            else:
                out += l * i
            l -= 8
            i += 1

        return out
