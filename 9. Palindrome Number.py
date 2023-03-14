class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_x= str(x)
        s_y= s_x[::-1]
        if s_x == s_y:
            return True
        else:
            return False
