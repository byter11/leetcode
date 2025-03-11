class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        vector<int> costs(s.size());
        for(int i=0; i<s.size(); i++) {
            costs[i] = abs(t[i] - s[i]);
        }

        // for(int &c: costs) cout << c << ':';
        // cout << '\n';

        int i = 0, j = 0, cost = costs[0], ans = 0;
        while(i < s.size() && j < s.size()) {
            // cout << cost << ":" << ans << ':' << i << ':' << j << '\n';
            if(cost > maxCost) {
                cost -= costs[i];
                i++;
            } else {
                j++;
                if (j < s.size())
                    cost += costs[j];
            }

            ans = max(ans, j-i);
        }

        return ans;
    }
};