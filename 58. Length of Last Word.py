class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split(" ")
        for i in range(len(word_list)):
            try:
                word_list.remove("")
            except:
                pass
        
        return len(word_list[-1])
