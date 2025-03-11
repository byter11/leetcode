class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n = nums.size();

        for(int i=0; i<n; i++) {
            int j = abs(nums[i])-1;
            if (nums[j] < 0) 
                return j + 1;
            else
                nums[j] = -nums[j];
        }
        return 0;
    }
};