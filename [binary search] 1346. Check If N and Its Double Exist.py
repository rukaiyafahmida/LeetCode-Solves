class Solution:
    def binary_search(self, nums: List[int], target: int, left: int, right: int) -> bool:
        if right < left:
            return False
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        if nums[mid] > target:
            return self.binary_search(nums, target, left, mid-1)
        if nums[mid] < target:
            return self.binary_search(nums, target, mid+1, right)

    def checkIfExist(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        arr.sort()
        if arr_len == 2:
            return arr[0]*2 == arr[1]
        div_arr = [w//2 for w in arr if w%2 == 0]
        length = len(div_arr)
        if length == 0:
            return False
        if div_arr.count(0)>1:
            return True
        for i in range(length):
            if div_arr[i] == 0:
                continue
            if self.binary_search(arr, div_arr[i], 0, arr_len-1):
                return True
        return False
