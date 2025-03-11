class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        int n = dist.size();
        vector<int> tick(n);
        
        for(int i=0; i<n; i++) {
            tick[i] = ceil((float)dist[i] / speed[i]);
            tick[i] = max(tick[i], 1);
        }


        for(int &v: tick) cout << v << ' ';
        cout << '\n';
        sort(tick.begin(), tick.end());
        

        int i;
        for(i=0; i<n; i++) {
            if(tick[i] - i < 1) break;
        }

        return i;
    }
};