class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        out = 0
        allowed = set(allowed)
        for word in words:
            if set(word).issubset(allowed):
                out += 1
        return out
