class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = s.size();
        vector<int> f(26, 0);
        int i = 0;
        int maxFreq = 0;
        int maxChar = s[0];
        int ans = 0;
        for(int j=0; j<n; j++) {
            int c = s[j] - 'A';
            f[c]++;
            if(f[c] >= maxFreq) {
                maxFreq = f[c];
                maxChar = c;
            }
            int len = j-i+1;
            int freq = max(maxFreq, f[c]);
            if(len - maxFreq <= k) {
                ans = max(ans, len);
            }
            else {
                f[s[i]-'A']--;
                i++;
                if(maxChar == s[i]-'A') maxFreq--;
            }
        }
        
        return ans;
    }
};