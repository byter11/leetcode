class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        int t = 0;
        vector<string> ans;
        for(int i=1; i<=n && t < target.size(); i++) {
            if(i == target[t]) {
                if(t==0) {
                    for(int j=1; j<i; j++) ans.push_back("Pop");
                }
                int j=i;
                while(t>0 && --j != target[t-1]) {
                        ans.push_back("Pop");
                }
                t++;
            }
            ans.push_back("Push");
        }

        return ans;
    }
};