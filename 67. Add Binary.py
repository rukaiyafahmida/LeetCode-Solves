class Solution:
    def binary_to_decimal(self, bin:str):
        decimal = 0
        length = len(bin)
        for i in range(length):
            decimal += int(bin[length-i-1]) * pow(2, i)
        return decimal
            

    def addBinary(self, a: str, b: str) -> str:
        int_a = self.binary_to_decimal(a)
        int_b = self.binary_to_decimal(b)
        ans = bin(int_a + int_b)
        return str(ans)[2:]
