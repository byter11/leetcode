class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        vector<int> ans;
        ans.push_back(pref[0]);
        int cum_xor = ans.back();
        for(int i=1; i<pref.size(); i++) {
            ans.push_back(cum_xor ^ pref[i]);
            cum_xor ^= ans.back();
        }

        return ans;
    }
};