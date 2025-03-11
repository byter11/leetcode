class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        int n = nums.size();
        int mx = *max_element(nums.begin(), nums.end());
        int mn = *min_element(nums.begin(), nums.end());
        
        vector<int> counts(mx-mn + 1, 0);
        for(int i=0; i<n; i++) {
            for(int j=i+1; j<n; j++) {
                counts[abs(nums[j] - nums[i])] += 1;
            }
        }

        for(int i=0; i<mx-mn + 1; i++) {
            k -= counts[i];
            if(k <= 0) return i;
        }

        return -1;
    }
};