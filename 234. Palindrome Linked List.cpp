/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        
        int n;
        ListNode* nxt = head;
        
        vector <int> ar;
        
        
        while( nxt != NULL)
        {
            ar.push_back(nxt->val);
            nxt=nxt->next;
        }
        int m=ar.size();
        n=m/2;
        for(int i=0;i<n;i++)
        {
            if(ar[i]==ar[m-i-1])
                continue;
            else
                return false;
        }
        return true;
        
    }
};
