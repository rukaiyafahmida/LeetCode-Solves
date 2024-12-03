class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_len = len(arr)
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
            if div_arr[i] in arr:
                return True
        return False
