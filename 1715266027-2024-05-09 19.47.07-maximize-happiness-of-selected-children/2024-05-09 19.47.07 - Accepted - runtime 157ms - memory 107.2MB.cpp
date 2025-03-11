class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        int n = happiness.size();
        long long sum = 0;
        for(int i=0; i<n; i++) sum += happiness[i];

        long long ans = 0;
        sort(happiness.begin(), happiness.end(), std::greater());

        for(int i=0; i<k; i++) {
            long long val = max(0, happiness[i] - i);
            if(sum - val <= 0) break;

            sum -= val;
            ans += val;
        }

        return ans;
    }
};