class Solution:
    def reverseBits(self, n: int) -> int:
        converted = str(bin(n))[2:]
        rev = "".join(reversed(converted)) + '0'*(32-len(converted))
        return int(rev,2)
