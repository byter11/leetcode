class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int n = strs.size();
        vector<vector<string>> res;
        vector<pair<string, int>> s_strs;
        for(int i=0; i<n; i++) {
            string s = strs[i];
            sort(s.begin(), s.end());
            s_strs.push_back({s, i});
        }
        sort(s_strs.begin(), s_strs.end());

        // for(auto s: s_strs) 
        //     cout << s.first << ' ' << s.second << " | ";

        vector<string> buf;
        buf.push_back(strs[s_strs[0].second]);
        for(int i=0; i<n-1; i++) {
            if(s_strs[i].first == s_strs[i+1].first)
                buf.push_back(strs[s_strs[i+1].second]);
            else {
                res.push_back(buf);
                buf.erase(buf.begin(), buf.end());
                buf.push_back(strs[s_strs[i+1].second]);
            }
        }

        res.push_back(buf);
        return res;
    }
};