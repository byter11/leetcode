class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        map<int,int> m;
        vector<pair<int,int>> v;
        vector<int> res(k);
        for(int i=0; i<n; i++)
            m[nums[i]]++;
        
        for(auto &p: m){
            v.push_back({p.second, p.first});
        }

        sort(v.begin(), v.end(), greater<pair<int,int>>());
        for(int i=0; i<k; i++) {
            res[i] = v[i].second;
        }
        return res;
    }
};