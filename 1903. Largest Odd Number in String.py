class Solution:
    def largestOddNumber(self, num: str) -> str:
        odds = ['1','3', '5', '7', '9']  
        len_num = len(num)
        for i in range(len_num-1, -1, -1):
            if num[i] in odds:
                return num[:i+1]
        return ""
