class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int prefixMod = 0, prefixSum = 0, ans = 0;
        int n = nums.size();
        unordered_map<int, int> seen;
        seen[prefixMod] = 1;
        cout << prefixMod << ' ';

        for(int i=0; i<n; i++) {
            prefixSum += nums[i];
            prefixMod = prefixSum % k;
            if(prefixMod < 0) prefixMod += k;
            // cout << prefixMod << ' ';
            if(seen.contains(prefixMod)) ans += seen[prefixMod];
            seen[prefixMod]++;
        }

        return ans;
    }
};

//   4 5 0 -2 -3 1
// 0 4 9 9  7  4 5
// 0 4 4 4  2  4 0