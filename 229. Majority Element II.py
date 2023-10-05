class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = len(nums)//3
        n = list(set(nums))

        return [a for a in n if nums.count(a)>count]







class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = floor(len(nums)/3)
        c = Counter(nums).items()

        out = [a for a, b in c if b>count]
        return out
