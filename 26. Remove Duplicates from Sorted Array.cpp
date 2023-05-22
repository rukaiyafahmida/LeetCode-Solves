class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        //int out=0;
        map<int,int> c;
        vector<int> out;
        
        for(int i=0; i<nums.size(); i++ )
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
        nums.clear();
        for(auto it : c)
        {
                nums.push_back(it.first);
        }
        return c.size();
    }
};
