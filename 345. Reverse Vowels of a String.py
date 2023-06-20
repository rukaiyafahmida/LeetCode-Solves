class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        list_of_vowel = [char for char in s if char in vowels]
        st = [char for char in s]
        for i, char in enumerate(s):
            if char in vowels:
                st[i] = list_of_vowel.pop()
        return "".join(st)
