class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        int zeroes = 0;
        if(nums.size() < 3) return res;
        unordered_set<int> t;
        unordered_map<int, int> m;

        for(int i=0; i<nums.size(); i++) {
            if(nums[i] == 0) zeroes++;
            else if(m.contains(nums[i])) t.insert(nums[i]);
            m[nums[i]] = i;
        }

        for(int i: t) {
            if(m.contains(-2*i)) res.push_back({i, i, -2*i});
        }

        for(int i=0; i<nums.size(); i++) {
            if(m[nums[i]] != i) continue;
            for(int j=i+1; j<nums.size(); j++) {
                if(m[nums[j]] != j) continue;
                int target = -(nums[i] + nums[j]);
                if( m[target] > j ) res.push_back({nums[i], nums[j], target});
            }
        }

        if(zeroes >= 3) res.push_back({0,0,0});
        return res;
    }
};