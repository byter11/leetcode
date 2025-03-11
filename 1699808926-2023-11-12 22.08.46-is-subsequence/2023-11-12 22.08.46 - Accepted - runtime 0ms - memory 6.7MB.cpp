class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, n = s.size();
        for(char &c: t) {
            if(c == s[i]) i++;
            if(i == n) break;
        }
        return i == n;
    }
};