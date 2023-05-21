class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int maxWel=-1,wel;
        int m = accounts.size(),n = accounts[0].size();
        
        for(int i=0; i<m; i++)
        {
            wel=0;
            for(int j=0; j<n; j++)
            {
                wel+=accounts[i][j];
            }

            maxWel=max(wel,maxWel);
        }
        
        return maxWel;
    }
};
