
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        if n == 1:
            return True
        ugly_list = [2,3,5]
        if n in ugly_list:
            return True
        factors = []
        i = 2
        while i * i <= n:       # check prime factors up to the square root of the number
            if n % i:
                i += 1
            else:
                n //= i
                if i in ugly_list:
                    factors.append(i)
                else:
                    return False
        if n > 1:
            if n in ugly_list:
                factors.append(n)
            else:
                return False
        return True   
