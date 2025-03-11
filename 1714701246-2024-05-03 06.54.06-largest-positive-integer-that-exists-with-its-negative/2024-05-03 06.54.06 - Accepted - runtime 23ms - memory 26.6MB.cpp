class Solution {
public:
    int findMaxK(vector<int>& nums) {
        unordered_set<int> s;
        for(int i=0; i<nums.size(); i++) {
            s.insert(nums[i]);
        }

        int max = -1;
        for(int i=0; i<nums.size(); i++) {
            if(nums[i] > max && s.contains(-nums[i])) max = abs(nums[i]);
        }

        return max;
    }
};