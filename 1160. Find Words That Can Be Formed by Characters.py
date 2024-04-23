from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        out = 0
        flag = False
        for word in words:
            char_list = [ch for ch in chars]
            for ch in word:
                try:
                    index = char_list.index(ch)
                    char_list.pop(index)
                    flag = True
                except:
                    flag = False
                    break
            if flag:
                out += len(word)

        return out
