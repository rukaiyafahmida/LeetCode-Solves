class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            index = word.index(ch)
            rev = word[:index+1]
            return rev[::-1]+word[index+1:]
        except:
            return word
