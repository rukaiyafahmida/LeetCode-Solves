class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        out=''
        n = min(strs, key=len)
        l=len(n)
        for i in range(l):
            if(all(n[i]==m[i] for m in strs)):
                out+=n[i]
            else:
                break
            
        return out
            
                    
                
