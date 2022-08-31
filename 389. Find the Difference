class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a=0
        b=0
        sLen= len(s)
        for i in range(0,len(t)):
            if(i<sLen):
                a+=ord(s[i])
            b+=ord(t[i])
        return chr(b-a)
