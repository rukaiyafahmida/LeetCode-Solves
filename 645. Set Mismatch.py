
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        length = len(nums)
        out = []
        for a, b in zip(nums, nums[1:]):
            if a == b:
                out.append(a)
                break
        temp = set(nums)
        y = [x + 1 for x in range(length)]
        t2 = set(y)
        x = t2.difference(temp)

        out.append(x.pop())
        return out
