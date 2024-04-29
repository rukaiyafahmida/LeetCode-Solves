
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        maps = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        out = maps[digits[:1]].copy()  # ['a', 'b', 'c']
        for j, d in enumerate(digits[1:]):
            for a in maps[d]:
                le = len(out)
                for i, v in enumerate(out):
                    if len(v) == j + 1:
                        out.append(v + a)
                        if i == le:
                            break
        ans = [x for x in out if len(x) == len(digits)]
        return ans
