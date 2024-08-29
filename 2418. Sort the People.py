class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [itm[1] for itm in sorted(zip(heights, names), reverse=True)]


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        end = [(heights[i], names[i]) for i in range(len(names))]
        end.sort(reverse=True)
        return [itm[1] for itm in end]
