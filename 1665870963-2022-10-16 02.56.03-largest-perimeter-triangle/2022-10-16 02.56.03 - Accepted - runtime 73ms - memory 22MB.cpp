class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size()-1;
        
        while(n-2 >= 0) {
            if (nums[n-2] > nums[n] - nums[n-1] &&
                nums[n-2] < nums[n] + nums[n-1] )
                return nums[n-2] + nums[n-1] + nums[n];
            n--;
        }
        
        return 0;
    }
};