class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ss1 = Counter((s1+" "+s2).split())
        item  = list(ss1.items())
        out = []
        for it in sorted(item, key=lambda x:x[1]):
            if it[1] == 1:
               out.append(it[0])
            else:
                break
        return out
