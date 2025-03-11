class Solution {
    int MOD = 1e9+7;
    vector<vector<vector<int>>> memo;
public:
    int checkRecord(int n) {
        memo = vector<vector<vector<int>>>(n+1);
        for(int i=0; i<n+1; i++) {
            memo[i] = vector<vector<int>>(3);
            for(int j=0; j<3; j++) {
                memo[i][j] = vector<int>(4, -1);
            }
        };

        return checkRecord(n, 1, 2) % MOD;
    }

    int checkRecord(int n, int a, int l) {
        if(n == 0) return 1;
        if(memo[n][a][l] != -1) return memo[n][a][l];

        int records = 0;
        records = (records + checkRecord(n-1, a, 2)) % MOD;
        if(a > 0) records = (records + checkRecord(n-1, a-1, 2)) % MOD;
        if(l > 0) records = (records + checkRecord(n-1, a, l-1)) % MOD;

        memo[n][a][l] = records;
        return records;
    }
};