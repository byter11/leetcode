class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        if(n < 2) return max(cost[0], cost[n-1]);
        
        for(int i = 2; i<n; i++) { 
            cost[i] = cost[i] + min (cost[i-1], cost[i-2]);
        } 
        return min(cost[n-1], cost[n-2]);
    }
};