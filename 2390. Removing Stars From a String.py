class Solution:
    def removeStars(self, s: str) -> str:
         out = []
         for char in s:
            if char == '*':
                out.pop()
            else:
                out.append(char)
         return "".join(out)
