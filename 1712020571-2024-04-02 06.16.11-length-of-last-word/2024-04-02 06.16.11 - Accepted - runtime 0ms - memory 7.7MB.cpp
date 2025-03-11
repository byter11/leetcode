class Solution {
public:
    int lengthOfLastWord(string s) {
        int cur = 0, last = 0;
        for(int i=0; i<s.size(); i++) {
            if(s[i] == ' ' && cur > 0) {
                last = cur;
                cur = 0;
            }
            else if(s[i] != ' ') cur++;
        }
        return cur > 0 ? cur : last;
    }
};