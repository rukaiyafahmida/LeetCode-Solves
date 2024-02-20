
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for x in nums:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)
        return even+odd
