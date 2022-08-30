class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        x=''
        for i in s:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
        
        for i in dic:
            if (dic[i]==1):
                x=i
                break
        if(x==''):
            return -1
        return s.find(x)
