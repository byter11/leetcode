class Solution {
public:
    int lengthOfLastWord(string s) {
        int space = -1;
        int n = s.size();
        while(s[n-1] == ' ') n--;

        for(int i=0; i<n; i++)
            if(s[i] == ' ') space = i;
        
        return n-space-1;
    }
};