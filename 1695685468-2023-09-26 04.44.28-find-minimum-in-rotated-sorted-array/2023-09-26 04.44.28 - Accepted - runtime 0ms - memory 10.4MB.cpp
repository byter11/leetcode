class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        int m = (l+r+1)/2;
        while(nums[l] < nums[m]) {
            l = m;
            m = (l+r+1)/2;
        }
        while(m > 0 && nums[m] > nums[m-1]) m--;

        return nums[m];
    }
};