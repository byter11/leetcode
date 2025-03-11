class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        if(n < 2) return;
        
        int s = 0, e = n-1;
        int i = 0;
        
        while(i <= e) {
            if(nums[i] == 2) {
                while(e >= 0 && nums[e] == 2) e--;
                if(e < 0) return;
                if(e>i)
                    swap(nums[e], nums[i]);
            }
            
            if(nums[i] == 0) {
                while(s < n && nums[s] == 0) s++;
                if(s >= n) return;
                if(s<i)
                    swap(nums[s], nums[i]);
            }
            
            i++;
        }
        
    }
};