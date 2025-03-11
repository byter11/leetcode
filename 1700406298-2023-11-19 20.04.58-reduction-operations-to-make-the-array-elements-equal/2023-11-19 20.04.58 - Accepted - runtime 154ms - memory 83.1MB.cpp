class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());
        int ops = 0;
        int largest = 1;

        for(int i=0; i<nums.size()-1; i++) {
            if(nums[i] > nums[i+1]) {
                ops += largest;
            }
            largest++;
        }

        return ops;
    }
};