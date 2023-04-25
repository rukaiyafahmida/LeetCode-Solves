class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        two = len(word2)
        one = len(word1)
        zipped = zip(word1, word2)
        out = [ x+y for x, y in zipped]
        out_str="".join(out)
        if two==one:
            return out_str
        elif two>one:
            return out_str+word2[one:]
        else:
            return out_str+word1[two:]
