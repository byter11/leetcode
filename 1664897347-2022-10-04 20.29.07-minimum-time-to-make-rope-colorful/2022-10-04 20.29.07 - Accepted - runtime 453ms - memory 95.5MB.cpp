class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int cur=0, sum=0, maxTime=0, time=0, n=colors.size();
        for(int i=0; i<n; i++) {
            if(colors[cur] != colors[i]) {
                time += sum - maxTime;
                cur = i;
                sum = neededTime[i];
                maxTime = sum;
            }
            else{
                sum += neededTime[i];
                maxTime = max(maxTime, neededTime[i]);    
            }
            
        }
        time += sum - maxTime;
        return time;
    }
};