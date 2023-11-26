class NumArray:
    arr = []
    def __init__(self, nums: List[int]):
        self.arr = nums

    def sumRange(self, left: int, right: int) -> int:
        output = 0
        for item in self.arr[left:right+1]:
            output += item
        return output
