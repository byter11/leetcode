class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        
        int n = nums.size();
        int oldSum = nums[0] + nums[1] + nums[2];
        
        for(int i=0; i<n-2; i++) {
            int twoSum = twoSumClosestRange(nums, target-nums[i], i+1, n-1);
            int newSum = nums[i] + twoSum;
            cout << nums[i] << ' ' << twoSum << ' ' << newSum << '\n';
            if(abs(target - oldSum) > abs(target - newSum))
                oldSum = newSum;
        }
        return oldSum;
    }
    
    int twoSumClosestRange(vector<int>& nums, int target, int i, int j) {
        int bestSum = nums[i] + nums[j];
        while(i<j) {
            int sum = nums[i] + nums[j];
            if(abs(target-bestSum) > abs(target-sum))
                bestSum = sum;
            if(sum == target) return sum;
            if(sum > target) j--;
            else i++;
        }
        return bestSum;
    }
};
    