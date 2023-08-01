class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [x for x in range(1,n+1)]
        com = list(itertools.combinations(arr,k))
        return com
