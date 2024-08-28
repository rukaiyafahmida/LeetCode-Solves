class Solution:
    def to_bin(self, num):
        binary = 0
        while num != 0:
            binary += num % 2
            num = num // 2
        return int(binary)

    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(0, n + 1):
            out.append(self.to_bin(i))
        return out

class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(0, 6):
            out.append([int(x) for x in bin(i)[2:]].count(1))
        return out
