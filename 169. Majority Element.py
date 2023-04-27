class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
        
        n = floor(len(nums)/2)
        
            
        for i in dic:
            if(dic[i]>n):
                x=i
        
        return x
