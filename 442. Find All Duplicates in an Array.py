class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        out = set()
        nums.sort()
        for x, y in zip(nums, nums[1:]):
            if x == y:
                out.add(x)
        return list(out)


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        check = [0] * (len(nums) + 1)
        ans = []
        for num in nums:
            if check[num] > 0:
                ans.append(num)
            else:
                check[num] += 1
        return ans
