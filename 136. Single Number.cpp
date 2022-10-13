class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        map<int,int> c;
        int x=-1;
        
        for(int i=0; i< nums.size(); i++)
        {
            if( c.find(nums[i]) == c.end() )
            {
                c[nums[i]]=1;
            }
            else
            {
                c[nums[i]]+=1;
            }
        }
            
        for(auto it : c)
        {
            if(it.second == 1)
                x = it.first;
        }
    
        
        return x;  
            
    }
};
