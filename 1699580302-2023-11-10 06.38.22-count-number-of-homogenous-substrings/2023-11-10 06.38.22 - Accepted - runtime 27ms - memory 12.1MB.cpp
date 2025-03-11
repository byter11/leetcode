class Solution {
    const int MOD = 1e9+7;
public:
    double nCr(int n, int r) {
        double sum = 1;
        for(int i = 1; i <= r; i++){
            sum = (sum * (n - r + i) / i);
        }

        return sum;
    }

    int countHomogenous(string s) {
        int n = s.size();
        int ans = n;

        int cur = 0;
        for(int i=1; i<n; i++) {
            if(s[i] == s[i-1]) {
                cur++;
            } else {
                ans += fmod(nCr(cur+1, 2), MOD);
                cur = 0;
            }
        }

        return fmod(ans + nCr(cur+1, 2), MOD);
    }
};