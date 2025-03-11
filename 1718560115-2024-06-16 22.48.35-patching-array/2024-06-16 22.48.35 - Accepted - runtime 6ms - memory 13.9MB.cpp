class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        int ans = 0, i = 0;
        long long sum = 1;
        while(sum <= n) {
            if(i < nums.size() && nums[i] <= sum) {
                sum += nums[i];
                i++;
            } else {
                ans++;
                sum += sum;
            }
        }

        return ans;
    }
};

// 1 2 3 3
// 1 2 3 3 (4 5 6 7 8 9)

// 1 2 3 6          n=20
// 1 2 3 6


// 1 6
// 1 2 6
// 1 2 (3) 6
// 1 2 (3) 4 6
// 1 2 (3) 4 (5) 6 (7) (8) (9) (10) (11) (12) (13) 14  22

// 1 2 = 3
// 1 2 3 = 1 2 3 4 5 6
// 1 2 3 4 = 1 2 3 4 5 6 7 8 9 10


// 1 = 1
// 2 = 3
// 3 = 6
// 4 = 10