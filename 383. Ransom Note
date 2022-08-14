class Solution {
public:
    int arN[26], arM[26];
    bool canConstruct(string ransomNote, string magazine) {
        
        for(int in=0;in<ransomNote.length();in++)
        {
            arN[ransomNote[in]-97]+=1;
        }

        for(int i=0;i<magazine.length();i++)
        {
              arM[magazine[i]-97]+=1;
        }

        for(int i=0;i<26;i++)
        {
            if(arM[i]-arN[i]>=0)
                continue;
            else
                return false;
        }
        return true;
    }
};
