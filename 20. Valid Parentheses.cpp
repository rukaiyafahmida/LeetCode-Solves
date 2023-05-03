class Solution {
public:
    bool isValid(string str) {
    stack<char> st;
        for(char& c : str) {
            if(c == '(' || c == '{' || c == '[')
                st.push(c);
            else {
                if(st.empty()) 
                    return false;
                const char t = st.top();
                if(c == ']' && t != '[') 
                    return false;
                if(c == '}' && t != '{') 
                    return false;
                if(c == ')' && t != '(') 
                    return false;
                st.pop();
            }
        }
        return st.empty();
    }
};
