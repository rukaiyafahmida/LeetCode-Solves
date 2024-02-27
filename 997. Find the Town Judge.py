# class Solution:
#     def findJudge(self, n: int, trust: List[List[int]]) -> int:
#         if not trust and n > 1:
#             if n != 1:
#                 return -1
#             else:
#                 return 1
#         tst_dict = dict()
#         for e in trust:
#             try:
#                 tst_dict[e[0]].append(e[1])
#             except:
#                 tst_dict[e[0]] = [e[1]]
#
#         cont = [i + 1 for i in range(n)]
#         c = set(cont)
#         x = set(tst_dict.keys())
#         xx = c.difference(x)
#         if len(xx) != 1:
#             return -1
#         char = xx.pop()
#         for lis in x:
#             if char not in tst_dict[lis]:
#                 return -1
#         return char


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tally = [0] * (n + 1)
        for i in trust:
            tally[i[0]] -= 1
            tally[i[1]] += 1
        for j in range(1, n + 1):
            if tally[j] == n - 1:
                return j
        return -1
