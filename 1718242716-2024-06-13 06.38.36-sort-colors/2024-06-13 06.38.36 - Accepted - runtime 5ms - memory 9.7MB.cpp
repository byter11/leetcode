class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        vector<int> counts(3, 0);

        for(int i=0; i<n; i++) counts[nums[i]]++;

        int i = 0;
        for(int j=0; j<3; j++) {
            while(counts[j] > 0) {
                nums[i] = j;
                counts[j]--;
                i++;
            }
        }
    }
};