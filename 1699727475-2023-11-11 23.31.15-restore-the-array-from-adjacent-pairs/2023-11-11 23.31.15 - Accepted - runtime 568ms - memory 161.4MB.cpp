class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        vector<int> ans;
        map<int, vector<int>> m;
        for(auto &v: adjacentPairs) {
            m[v[0]].push_back(v[1]);
            m[v[1]].push_back(v[0]);
        }
        for(auto &p: m) {
            if(p.second.size() == 1) {
                ans.push_back(p.first);
                break;
            }
        }

        dfs(m, ans);

        return ans;
    }

    void dfs(map<int, vector<int>> &m, vector<int> &ans) {
        vector<int> i = m[ans.back()];
        m[ans.back()] = {};

        for(auto &v: i) {
            if(m[v].size() > 0) ans.push_back(v);
            dfs(m, ans);
        }
    }
};