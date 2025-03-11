class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        // [100,-1,-100,-1,100], k=2
        // [100,99, 0,  98,198]
        const int n = nums.size();
        deque dq{0};
        
        for(int i=1; i<n; i++){
            nums[i] = nums[i] + nums[dq.back()];
            
            while(!dq.empty() && nums[dq.front()] <= nums[i])
                dq.pop_front();
            
            dq.push_front(i);
            
            while(!dq.empty() && dq.back() <= i-k) 
                dq.pop_back();
        }
    
        for(int &i: nums) cout << i << ' ';
        return nums[n-1];
    }
};