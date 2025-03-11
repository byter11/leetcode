class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // [1,2,3,4]
        int n = nums.size();
        
        // [1,2, 6, 24]
        vector<int> out;
        out.push_back(nums[0]);
        for(int i=1; i<n; i++) {
            out.push_back(out[i-1] * nums[i]);
        }
        
        // [24,24,12,4]
        for(int i=n-2; i>=0; i--) {
            nums[i] = nums[i+1] * nums[i];
        }
        
        for(int i=n-1; i>=0; i--) {
            out[i] = (i-1 >=0 ? out[i-1] : 1) * (i+1 < n ? nums[i+1] : 1);
        }
        
        return out;
    }
};