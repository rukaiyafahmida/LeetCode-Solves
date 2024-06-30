class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        lis = [Counter(w).items() for w in words]
        out = []
        for key in lis[0].mapping.keys():
            mini = 101
            present = True
            for lisr in lis[1:]:
                if key not in lisr.mapping.keys():
                    present = False
                    break
                mini = min(mini, min(lisr.mapping.get(key), lis[0].mapping.get(key)))
            if present:
                out.extend(key * mini)
        return out
