class Solution {
public:
    
    static bool compare(pair<int, int> x, pair<int, int> y) {
        if(x.first!=y.first)
            return x.first< y.first;
        else    
            return x.second< y.second;
            
    }
        
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
    int num;
    int m = mat.size(), n = mat[0].size();
                //val, no
    vector<pair<int, int>> row;


    for(int i=0; i<m; i++)
    {
        num=0;
        for(int j=0; j<n; j++)
        {
            num += mat[i][j];
        }
        row.push_back(make_pair(num,i));
    }

        sort(row.begin(), row.end(), compare);
        vector<int> ans;
        for(int i=0;i<k;i++)
        {
            ans.push_back(row[i].second);
        }
       return ans;

    }
};
