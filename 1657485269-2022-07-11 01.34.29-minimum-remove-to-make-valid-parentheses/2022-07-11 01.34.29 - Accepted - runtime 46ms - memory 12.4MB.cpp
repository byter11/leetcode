class Solution {
public:
    string minRemoveToMakeValid(string s) {
        string ans = "";
        vector<int> stack;
        
        for(int i=0; i<s.size(); i++) {
            if(s[i] == '(') stack.push_back(i);
            else if(s[i] == ')') {
                if(!stack.empty()){
                    ans += s[i];
                    stack.pop_back();
                }
            }
            if(s[i] != ')')
                ans += s[i];
        }
        
        string f = "";
        for(int i=ans.size()-1; i>=0; i--) {
            if(ans[i] == '(' && !stack.empty()) stack.pop_back();
            else f += ans[i];
        }
            
        reverse(f.begin(), f.end());
        return f;
    }
};