class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        ans[n-1] = nums[n-1];
        for(int i=n-2; i>=0; i--)
            ans[i] = nums[i] * ans[i+1];

        for(int i=1; i<n; i++)
            nums[i] *= nums[i-1];

        // for(int i=0; i<n; i++)
        //     cout << nums[i] << ' ';
        // cout << '\n';
        // for(int i=0; i<n; i++)
        //     cout << ans[i] << ' ';

        ans[0] = ans[1];
        for(int i=1; i<n-1; i++) {
            ans[i] = nums[i-1]*ans[i+1];
        }
        ans[n-1] = nums[n-2];

        return ans;
    }
};
