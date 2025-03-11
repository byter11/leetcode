class Solution {
public:
    int specialArray(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());

        int ok = 0;
        int i = 0;
        while(i < nums.size() && nums[i] > i) {
            i++;
            ok = 1;
        }

        if(!ok) return -1;

        if(i < nums.size() && nums[i] == i) return -1;
        return i;
    }
};

// 4 4 3 0 0
// 0 
// 1
// 2
// 3
// 