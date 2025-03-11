class Solution {
public:
    int scoreOfString(string s) {
        int score = 0, n = s.size();

        for(int i=1; i<n; i++) {
            score += abs(s[i-1] - s[i]);
        }

        return score;
    }
};